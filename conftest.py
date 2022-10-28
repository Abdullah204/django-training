import pytest
from rest_framework.test import APIClient
from users.models import User
@pytest.fixture
def auth_client():
    
    def api_client(user = None):
        if(user is None):
            user = User(username = "arbitrary user" , password = "arbitrary passsword" , email = "arbit@gmail.com")
        client = APIClient()
        return client
    return api_client