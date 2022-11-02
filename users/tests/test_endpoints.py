import email
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from django.contrib.auth import get_user_model
from users.views import UserDetailView
import pytest
@pytest.mark.django_db
def test_UserDetailViewGET(client):
    register_data = {
    "username" : "useruser",
    "email" : "useruser@gmail.com",
    "password" : "adwmfqwpfqmpfqwf",
    "confirm_password" : "adwmfqwpfqmpfqwf"
    }
    client.post('http://localhost:8000/authentication/register/',register_data)
    response = client.get('http://localhost:8000/users/1/') 
    assert response.data == {'bio': '', 'email': 'useruser@gmail.com', 'id': 1, 'username': 'useruser'}


def test_UserDetailViewGETNotFound(client):
    response = client.get('http://localhost:8000/users/1/') 
    assert response.status_code == 404

@pytest.mark.django_db
def test_UserDetailViewPUT(client):


    register_data = {
    "username" : "useruser",
    "email" : "useruser@gmail.com",
    "password" : "adwmfqwpfqmpfqwf",
    "confirm_password" : "adwmfqwpfqmpfqwf"
    }
    client.post('http://localhost:8000/authentication/register/' , register_data)
    user = get_user_model().objects.get(pk =1)

    put_data = {
        "bio" : "newBIO",
        "username" : "javed2",
        "email" : "javed2@javed.com",
        "password" :"sdadadadasda"
    }
    client.force_authenticate(user = user)
    response= client.put('http://localhost:8000/users/1/',put_data)
    
    
    assert response.data == {'bio': 'newBIO', 'email': 'javed2@javed.com', 'id': 1, 'username': 'javed2'}

@pytest.mark.django_db
def test_UserDetailViewPUTUsernameMissing(client , user):
    put_data = {
        "bio" : "newBIO",
        "email" : "javed2@javed.com",
        "password" :"sdadadadasda"
    }
    client.force_authenticate(user = user)
    response= client.put('http://localhost:8000/users/1/',put_data)
    assert response.status_code == 400


@pytest.mark.django_db
def test_UserDetailViewPUTPasswordMissing(client,user):
    put_data = {
        "bio" : "newBIO",
        "email" : "javed2@javed.com",
        "username" :"sdadadadasda"
    }
    client.force_authenticate(user = user)
    response= client.put('http://localhost:8000/users/1/',put_data)
    assert response.status_code == 400



@pytest.mark.django_db
def test_UserDetailViewPUTDifferentID(client ,user):
    put_data = {
        "bio" : "newBIO",
        "username" : "javed2",
        "email" : "javed2@javed.com",
        "password" :"sdadadadasda"
    }
    client.force_authenticate(user = user)
    response= client.put('http://localhost:8000/users/2/',put_data)
    assert response.status_code == 401


@pytest.mark.django_db
def test_UserDetailViewPUTUnavailableID(client , user):
    put_data = {
        "bio" : "newBIO",
        "email" : "javed2@javed.com",
        "username" :"sdadadadasda"
    }
    user.pk = 5
    client.force_authenticate(user = user)
    response= client.put('http://localhost:8000/users/5/',put_data)
    assert response.status_code == 404


@pytest.mark.django_db
def test_UserDetailViewPATCHUnavailableID(client , user):
    put_data = {
        "bio" : "newBIO",
        "email" : "javed2@javed.com",
        "username" :"sdadadadasda"
    }
    user.pk = 5
    client.force_authenticate(user = user)
    response= client.patch('http://localhost:8000/users/5/',put_data)
    assert response.status_code == 404


@pytest.mark.django_db
def test_UserDetailViewPATCHDifferentID(client , user):
    put_data = {
        "bio" : "newBIO",
        "username" : "javed2",
        "email" : "javed2@javed.com",
        "password" :"sdadadadasda"
    }
    client.force_authenticate(user = user)
    response= client.patch('http://localhost:8000/users/2/',put_data)
    assert response.status_code == 401



@pytest.mark.django_db
def test_UserDetailViewPATCHPartialData(client,user):
    put_data = {
        "bio" : "newBIO",
        "username" : "javed2",
    }
    client.force_authenticate(user = user)
    response= client.patch('http://localhost:8000/users/1/',put_data)
    assert response.data == {'bio': 'newBIO', 'email': 'ahmed@gmail.com', 'id': 1, 'username': 'javed2'}


@pytest.mark.django_db
def test_UserDetailViewPATCHFullData(client,user):
    put_data = {
        "bio" : "newBIO",
        "username" : "javed2",
        "email" : "javed2@javed.com",
        "password" :"sdadadadasda"
    }
    client.force_authenticate(user = user)
    response= client.patch('http://localhost:8000/users/1/',put_data)
    assert response.data == {'bio': 'newBIO', 'email': 'javed2@javed.com', 'id': 1, 'username': 'javed2'}