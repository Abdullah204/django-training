import pytest
from rest_framework.test import APIClient
from users.models import User
from artists.models import Artist
from albums.models import Album
from authentication.serializers import UserRegistrationSerializer

@pytest.fixture
def user():
    user = User.objects.create_user('ahmed', 'ahmed@gmail.com', 'Ahmed_1234')
    return user

@pytest.fixture
def client():
    return APIClient()

 
@pytest.fixture
def auth_client(user, client):
    login_response = client.post('http://localhost:8000/authentication/login/', dict(username="ahmed", password="Ahmed_1234"))

    token = login_response.data["token"]

    client.credentials(HTTP_AUTHORIZATION='Token ' + token)

    return client

@pytest.fixture
def get_client(user):
    def api_client(user_instance=None):
        if user_instance is None:
            client = APIClient()

            login_response = client.post('http://localhost:8000/authentication/login/', dict(username="ahmed", password="Ahmed_1234"))

            token = login_response.data["token"]

            client.credentials(HTTP_AUTHORIZATION='Token ' + token)

            return client, user.id
        else:
            client = APIClient()
            
            random_user = User.objects.create_user(user_instance['username'], user_instance['email'], user_instance['password'])

            login_response = client.post('http://localhost:8000/authentication/login/', dict(username=user_instance["username"], password=user_instance["password"]))

            token = login_response.data["token"]

            client.credentials(HTTP_AUTHORIZATION='Token ' + token)

            return client, random_user.id
    
    return api_client



@pytest.fixture
def artist(user):
    artist = Artist.objects.create(stage_name = 'artist1',social_link_field =  'http://www.artist1.com', user = user)
    return artist

@pytest.fixture
def album(artist):
    album = Album.objects.create(name = "album1" , cost = 11.2 , release_datetime = "2001-12-04" , artist = artist ,is_approved  = True)
    return album

