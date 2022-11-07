from albums.serializers import AlbumSerializer , AlbumRequestSerializer
import pytest
@pytest.mark.django_db
def test_album_serializer_valid(artist):
    data = dict(name = "album1" ,release_datetime = "2022-07-01" , cost =12 , artist = artist)
    serializer = AlbumSerializer(data = data)
    assert serializer.is_valid()
    assert serializer.data == {'cost': '12.00' ,
         'release_datetime': '2022-07-01T00:00:00Z' ,
         'artist': 1
         ,'name' : 'album1'}
    assert serializer.errors == {}


@pytest.mark.django_db
def test_album_serializer_invalid(artist):
    data = dict(name = "album1" ,release_datetime = "2022-07-01" , cost =12 )
    serializer = AlbumSerializer(data = data)
    assert(not serializer.is_valid())
    data = dict(name = "album1" ,artist = artist , cost =12 )
    assert(not serializer.is_valid())

@pytest.mark.django_db
def test_album_request_serializer_valid(artist):
    data = dict(name = "album1" ,release_datetime = "2022-07-01" , cost =12 )
    serializer = AlbumRequestSerializer(data=data ,context={'artist': artist})
    assert serializer.is_valid()
    assert serializer.data == {'cost': '12.00' ,
         'release_datetime': '2022-07-01T00:00:00Z' ,
         'name' : 'album1'}
    assert serializer.errors == {}

@pytest.mark.django_db
def test_album_request_serializer_invalid(artist):
    data = dict(name = "album1" ,release_datetime = "2022-07-01" )
    serializer = AlbumRequestSerializer(data=data )
    assert not serializer.is_valid()
    data = dict(name = "album1" ,cost =12 )
    serializer = AlbumRequestSerializer(data=data )
    assert not serializer.is_valid()



    
    

