import pytest
from collections import OrderedDict
@pytest.mark.django_db
def test_artist_create_album(artist,auth_client):
    album = dict(name = 'testalbum' , release_datetime = '2003-06-06' , cost = 11 )
    response = auth_client.post('http://localhost:8000/albums/',album)
    assert response.status_code == 201 
    assert response.data == {'cost': '11.00',
         'name': 'testalbum',
          'release_datetime': '2003-06-06T00:00:00Z'}

@pytest.mark.django_db
def test_user_create_album(user  , auth_client): # normal user that is not an artist
    album = dict(name = 'testalbum' , release_datetime = '2003-06-06' , cost = 11 )
    response = auth_client.post('http://localhost:8000/albums/',album)
    assert response.status_code == 403

@pytest.mark.django_db
def test_artist_create_album_missing_field(artist,auth_client):
    album = dict(name = 'testalbum' , release_datetime = '2003-06-06'  )
    response = auth_client.post('http://localhost:8000/albums/',album)
    assert response.status_code == 400

@pytest.mark.django_db
def test_unauthenticated_create_album(user , client):
    album = dict(name = 'testalbum' , release_datetime = '2003-06-06' , cost = 11 )
    response = client.post('http://localhost:8000/albums/',album)
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_albums_unauthenticated(client,album):
    response = client.get('http://localhost:8000/albums/')
    assert response.data == OrderedDict([('count', 1), ('next', None), ('previous', None), ('results', [OrderedDict([('name', 'album1'), ('release_datetime', '2001-12-04T00:00:00Z'), ('cost', '11.20'), ('artist', 1)])])])


@pytest.mark.django_db
def test_get_albums_authenticated(auth_client,album):
    response = auth_client.get('http://localhost:8000/albums/')
    assert response.data == OrderedDict([('count', 1), ('next', None), ('previous', None), ('results', [OrderedDict([('name', 'album1'), ('release_datetime', '2001-12-04T00:00:00Z'), ('cost', '11.20'), ('artist', 1)])])])
