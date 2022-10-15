from dataclasses import field
from django.forms import ModelForm
from .models import Album,Song
from django import forms
from .widget import MyDateTimeInput
from django.contrib import admin


    

class AlbumForm (ModelForm):
    class Meta:
        model = Album
        fields = '__all__'



