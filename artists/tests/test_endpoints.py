import email
from rest_framework.test import APIRequestFactory
from rest_framework.test import RequestsClient
import pytest
from rest_framework.test import APIClient
import sys, os
from users.models import User
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ErrorDetail
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from artists.models import Artist
from collections import OrderedDict

@pytest.mark.django_db
def test_ArtistListGet(client , user):
    Artist.objects.create(stage_name = 'artist1' , social_link_field = 'http://www.artist1.com' , user =user)
    response = client.get('http://localhost:8000/artists/')
    assert response.data  == [OrderedDict([('user', 1), ('stage_name', 'artist1'), ('social_link_field', 'http://www.artist1.com')])]


@pytest.mark.django_db
def test_ArtistListPut(client ,user):
    post_data = dict(user = user.id ,stage_name = "abc123" , social_link_field = "http://www.artist.com")
        
    response = client.post('http://localhost:8000/artists/',post_data)
    assert response.data == {'user': 1 , 'stage_name': 'abc123', 'social_link_field': 'http://www.artist.com'}

@pytest.mark.django_db
def test_ArtistListPutInvalidData(client):
    post_data = {
        "stage_name" : "abc123",
        "social_link_field" : "accacsac"
    }
    response = client.post('http://localhost:8000/artists/',post_data)
    assert response.status_code == 400


@pytest.mark.django_db
def test_ArtistListPutMissingData(client):
    post_data = {
        "social_link_field" : "accacsac"
    }
    response = client.post('http://localhost:8000/artists/',post_data)
    assert response.status_code == 400


@pytest.mark.django_db
def test_ArtistListPutDuplicateStageName(client , user):
    data =dict(stage_name = "abc123" , social_link_field ="http://www.artist.com" , user = user)
    
    response = client.post('http://localhost:8000/artists/',data)
    response = client.post('http://localhost:8000/artists/',data)
    assert response.status_code == 400