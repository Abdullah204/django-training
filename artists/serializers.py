from rest_framework import serializers
from artists.models import Artist


class ArtistSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    stage_name = serializers.CharField(allow_blank = False , max_length = 80)
    social_link_field = serializers.URLField(required=True, allow_blank=True)

    def validate_stage_name(self,value):
        if Artist.objects.filter(stage_name__exact=value).exists():
            raise serializers.ValidationError("Name already exists!")
        return value
    def create(self, validated_data):
        """
        Create and return a new `Artist` instance, given the validated data.
        """
        return Artist.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Artist` instance, given the validated data.
        """
        instance.stage_name = validated_data.get('stage_name',instance.stage_name)
        instance.social_link_field = validated_data.get('social_link_field',instance.social_link_field)
       
        instance.save()
        return instance