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

@pytest.mark.django_db
def test_ArtistListGet(auth_client):
    
    client = auth_client()
    response = client.get('http://localhost:8000/artists/')
    assert response.data  == []


@pytest.mark.django_db
def test_ArtistListPut(auth_client):
    
    client = auth_client()
    post_data = {
        "stage_name" : "abc123",
        "social_link_field" : "http://www.artist.com"
    }
    response = client.post('http://localhost:8000/artists/',post_data)
    assert response.data == {'id': 1, 'stage_name': 'abc123', 'social_link_field': 'http://www.artist.com'}

@pytest.mark.django_db
def test_ArtistListPutInvalidData(auth_client):
    
    client = auth_client()
    post_data = {
        "stage_name" : "abc123",
        "social_link_field" : "accacsac"
    }
    response = client.post('http://localhost:8000/artists/',post_data)
    assert response.status_code == 400


@pytest.mark.django_db
def test_ArtistListPutMissingData(auth_client):
    
    client = auth_client()
    post_data = {
        "social_link_field" : "accacsac"
    }
    response = client.post('http://localhost:8000/artists/',post_data)
    assert response.status_code == 400


@pytest.mark.django_db
def test_ArtistListPutDuplicateStageName(auth_client):
    
    client = auth_client()
    post_data = {
        "stage_name" : "abc123",
        "social_link_field" : "http://www.artist.com"
    }
    response = client.post('http://localhost:8000/artists/',post_data)
    response = client.post('http://localhost:8000/artists/',post_data)
    assert response.status_code == 400