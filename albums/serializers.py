from rest_framework import serializers
from albums.models import Album
from artists.models import Artist
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['name' , 'release_datetime' , 'cost' , 'artist']

class AlbumRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['name' , 'release_datetime' , 'cost']
    def create(self, validated_data):
        return Album.objects.create(name=validated_data['name'], release_datetime=validated_data['release_datetime'], cost=validated_data['cost'], artist=self.context['artist'])
