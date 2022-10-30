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
def test_authenticatedRegisterView(auth_client):
    user = User.objects.create(username = "authenticated" , password = "adqwifqifmq" 
    , email = "adwada@gmail.com" )
    client = auth_client(user)
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
def test_unAuthenticatedRegisterViewWithValidData():
 
    client = APIClient()

    register_data = {
    "username" : "MegaCoredadp",
    "email" : "activedade@gmail.com",
    "password" : "adwmfqwpfqmpfqwf",
    "confirm_password" : "adwmfqwpfqmpfqwf"
    }
    
    response = client.post('http://localhost:8000/authentication/register/',register_data)
    assert response.status_code == 200


def test_RegisterUsernameRequired():
    client = APIClient()

    register_data = {
    "email" : "activedadsadde@gmail.com",
    "password" : "adwmfqwpfqmpfqwf",
    "confirm_password" : "adwmfqwpfqmpfqwf"
    }
    response = client.post('http://localhost:8000/authentication/register/',register_data)
    assert response.data == {'username': [ErrorDetail(string='This field is required.', code='required')]}

def test_RegisterPasswordRequired():
    client = APIClient()

    register_data = {
    "email" : "activedade@gmail.com",
    "username" : "adwmfqwpfqmpfqwf",
    "confirm_password" : "adwmfqwpfqmpfqwf"
    }
    response = client.post('http://localhost:8000/authentication/register/',register_data)
    assert response.data == {'password': [ErrorDetail(string='This field is required.', code='required')]}


def test_RegisterConfirm_PasswordRequired():
    client = APIClient()

    register_data = {
    "email" : "activedade@gmail.com",
    "username" : "adwmfqwpfqmpfqwf",
    "password" : "adwmfqwpfqmpfqwf"
    }
    response = client.post('http://localhost:8000/authentication/register/',register_data)
    assert response.data == {'confirm_password': [ErrorDetail(string='This field is required.', code='required')]}

def test_RegisterConfirmEmailRequired():
    client = APIClient()

    register_data = {
    "confirm_password" : "adwmfqwpfqmpfqwf",
    "username" : "adqwdqdqwdqq",
    "password" : "adwmfqwpfqmpfqwf"
    }
    response = client.post('http://localhost:8000/authentication/register/',register_data)
    assert response.data == {'email': [ErrorDetail(string='This field is required.', code='required')]}


@pytest.mark.django_db
def test_adminRegisterView(auth_client):
    user = User.objects.create(username = "authenticated" , password = "adqwifqifmq" 
    , email = "adwada@gmail.com" )
    user.is_superuser = True
    client = auth_client(user)
    register_data = {
    "username" : "MegaCoredadp",
    "email" : "activedade@gmail.com",
    "password" : "adwmfqwpfqmpfqwf",
    "confirm_password" : "adwmfqwpfqmpfqwf"
    }
    response = client.post('http://localhost:8000/authentication/register/',register_data)
    assert response.status_code  == 200


@pytest.mark.django_db
def test_authenticatedLoginView(auth_client):
    client = APIClient()

    register_data = {
    "username" : "MegaCoredadp",
    "email" : "activedade@gmail.com",
    "password" : "adwmfqwpfqmpfqwf",
    "confirm_password" : "adwmfqwpfqmpfqwf"
    }
    login_data = {
    "username" : "MegaCoredadp",
    "password" : "adwmfqwpfqmpfqwf",
    }
    client.post('http://localhost:8000/authentication/register/',register_data) 
    response = client.post('http://localhost:8000/authentication/login/',login_data) 
    assert response.status_code  == 200



@pytest.mark.django_db
def test_authenticatedLoginViewIncorrectPassword(auth_client):
    client = APIClient()

    register_data = {
    "username" : "MegaCoredadp",
    "email" : "activedade@gmail.com",
    "password" : "adwmfqwpfqmpfqwf",
    "confirm_password" : "adwmfqwpfqmpfqwf"
    }
    login_data = {
    "username" : "MegaCoredadp",
    "password" : "adwmfqwpfqmpf",
    }
    client.post('http://localhost:8000/authentication/register/',register_data) 
    response = client.post('http://localhost:8000/authentication/login/',login_data) 
    assert response.status_code  == 400

@pytest.mark.django_db
def test_authenticatedLoginViewIncorrectUsername(auth_client):
    client = APIClient()

    register_data = {
    "username" : "MegaCoredadp",
    "email" : "activedade@gmail.com",
    "password" : "adwmfqwpfqmpfqwf",
    "confirm_password" : "adwmfqwpfqmpfqwf"
    }
    login_data = {
    "username" : "MegaCored",
    "password" : "adwmfqwpfqmpf",
    }
    client.post('http://localhost:8000/authentication/register/',register_data) 
    response = client.post('http://localhost:8000/authentication/login/',login_data) 
    assert response.status_code  == 400


@pytest.mark.django_db
def test_authenticatedLoginData(auth_client):
    client = APIClient()

    register_data = {
    "username" : "MegaCoredadp",
    "email" : "activedade@gmail.com",
    "password" : "adwmfqwpfqmpfqwf",
    "confirm_password" : "adwmfqwpfqmpfqwf"
    }
    login_data = {
    "username" : "MegaCoredadp",
    "password" : "adwmfqwpfqmpfqwf",
    }
    client.post('http://localhost:8000/authentication/register/',register_data) 
    response = client.post('http://localhost:8000/authentication/login/',login_data) 
    assert response.data ["username"] == "MegaCoredadp" and response.data ["bio"] == '' and response.data ["email"] == "activedade@gmail.com"  and response.data ["token"] 



@pytest.mark.django_db
def test_unauthenticatedLogout():
    client = APIClient()
    response = client.post('http://localhost:8000/authentication/logout/') 
    assert response.status_code == 401


@pytest.mark.django_db
def test_authenticatedLogout():

    client = APIClient()
    register_data = {
    "username" : "useruser",
    "email" : "useruser@gmail.com",
    "password" : "adwmfqwpfqmpfqwf",
    "confirm_password" : "adwmfqwpfqmpfqwf"
    }
    login_data = {
    "username" : "useruser",
    "password" : "adwmfqwpfqmpfqwf",
    }
    client.post('http://localhost:8000/authentication/register/',register_data)
    login_response = client.post('http://localhost:8000/authentication/login/',login_data) 
    token = login_response.data["token"]
    client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    response = client.post('http://localhost:8000/authentication/logout/') 
    assert response.status_code == 204