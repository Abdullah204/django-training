from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth import password_validation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username' ,'email' , 'bio' , 'password']
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    def validate(self, data):
        password_validation.MinimumLengthValidator().validate(data.get('password'))
        password_validation.CommonPasswordValidator().validate(data.get('password'))
        password_validation.NumericPasswordValidator().validate(data.get('password'))
        password_validation.UserAttributeSimilarityValidator().validate(data.get('password'))
        return super().validate(data)
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.save()
        return instance