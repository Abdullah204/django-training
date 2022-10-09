from dataclasses import field
from django.forms import ModelForm
from .models import Album
from django import forms
from .widget import MyDateTimeInput
class AlbumForm (ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'release_datetime' : MyDateTimeInput()
        }