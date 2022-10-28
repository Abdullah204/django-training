# from users.tests.conftest import auth_client
import email
from rest_framework.test import APIRequestFactory
from rest_framework.test import RequestsClient
import pytest
from rest_framework.test import APIClient
import sys, os
from users.models import User
from django.contrib.auth import get_user_model



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
    print(response.content)
    assert response.status_code == 200

