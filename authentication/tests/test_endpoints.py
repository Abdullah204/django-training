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
def test_authenticatedRegisterView(client,user):
    client.force_authenticate(user = user)
    response = client.post('http://localhost:8000/authentication/register/',json={
    'username': 'MegaCorp',
    'email': 'active@gmail.com',
    'password' : "adwmfqwpfqmpfqwf",
    'confirm_passsword' : "adwmfqwpfqmpfqwf",
    
})
    assert response.status_code  == 403

@pytest.mark.django_db
def test_unAuthenticatedRegisterView():
    # 400 because request has permission but data not passed
    client = RequestsClient()
    response = client.post('http://localhost:8000/authentication/register/')
    assert response.status_code == 400


@pytest.mark.django_db
def test_unAuthenticatedRegisterViewWithValidData(client):
    register_data = {
    "username" : "MegaCoredadp",
    "email" : "activedade@gmail.com",
    "password" : "adwmfqwpfqmpfqwf",
    "confirm_password" : "adwmfqwpfqmpfqwf"
    }
    
    response = client.post('http://localhost:8000/authentication/register/',register_data)
    assert response.status_code == 200


def test_RegisterUsernameRequired(client):
    register_data = {
    "email" : "activedadsadde@gmail.com",
    "password" : "adwmfqwpfqmpfqwf",
    "confirm_password" : "adwmfqwpfqmpfqwf"
    }
    response = client.post('http://localhost:8000/authentication/register/',register_data)
    assert response.data == {'username': [ErrorDetail(string='This field is required.', code='required')]}

def test_RegisterPasswordRequired(client):
    register_data = {
    "email" : "activedade@gmail.com",
    "username" : "adwmfqwpfqmpfqwf",
    "confirm_password" : "adwmfqwpfqmpfqwf"
    }
    response = client.post('http://localhost:8000/authentication/register/',register_data)
    assert response.data == {'password': [ErrorDetail(string='This field is required.', code='required')]}


def test_RegisterConfirm_PasswordRequired(client):
    register_data = {
    "email" : "activedade@gmail.com",
    "username" : "adwmfqwpfqmpfqwf",
    "password" : "adwmfqwpfqmpfqwf"
    }
    response = client.post('http://localhost:8000/authentication/register/',register_data)
    assert response.data == {'confirm_password': [ErrorDetail(string='This field is required.', code='required')]}

def test_RegisterConfirmEmailRequired(client):
    register_data = {
    "confirm_password" : "adwmfqwpfqmpfqwf",
    "username" : "adqwdqdqwdqq",
    "password" : "adwmfqwpfqmpfqwf"
    }
    response = client.post('http://localhost:8000/authentication/register/',register_data)
    assert response.data == {'email': [ErrorDetail(string='This field is required.', code='required')]}


@pytest.mark.django_db
def test_adminRegisterView(client, user):
    user.is_superuser = True
    register_data = {
    "username" : "MegaCoredadp",
    "email" : "activedade@gmail.com",
    "password" : "adwmfqwpfqmpfqwf",
    "confirm_password" : "adwmfqwpfqmpfqwf"
    }
    response = client.post('http://localhost:8000/authentication/register/',register_data)
    assert response.status_code  == 200


@pytest.mark.django_db
def test_authenticatedLoginView(client , user):
    login_data = dict(username="ahmed", password="Ahmed_1234")

    response = client.post('http://localhost:8000/authentication/login/',login_data) 
    assert response.status_code  == 200



@pytest.mark.django_db
def test_authenticatedLoginViewIncorrectPassword(client,user):
    login_data = {
    "username" : user.username,
    "password" : user.password+"dsadasd",
    }
    response = client.post('http://localhost:8000/authentication/login/',login_data)  
    assert response.status_code  == 400

@pytest.mark.django_db
def test_authenticatedLoginViewIncorrectUsername(client,user):
    login_data = {
    "username" : user.username+"dsadasd",
    "password" : user.password,
    }
    response = client.post('http://localhost:8000/authentication/login/',login_data)  
    assert response.status_code  == 400


@pytest.mark.django_db
def test_authenticatedLoginData(user,client):
    login_data = dict(username="ahmed", password="Ahmed_1234")
    response = client.post('http://localhost:8000/authentication/login/',login_data) 
    print(response.data)
    assert response.data ["username"] == user.username and response.data ["bio"] == user.bio and response.data ["email"] == user.email  and response.data ["token"] 



@pytest.mark.django_db
def test_unauthenticatedLogout(client):
    response = client.post('http://localhost:8000/authentication/logout/') 
    assert response.status_code == 401


@pytest.mark.django_db
def test_authenticatedLogout(get_client,auth_client):
    response = auth_client.post('http://localhost:8000/authentication/logout/') 
    assert response.status_code == 204