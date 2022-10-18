from typing_extensions import Required
from unicodedata import decimal
from django.db import models
import datetime
from django.utils import timezone
from artists.models import Artist
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
import os
from django.core.exceptions import ValidationError
from django import forms


def validate_file_extension(value):
        ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
        valid_extensions = ['.wav', '.mp3']
        if not ext.lower() in valid_extensions:
            raise ValidationError('Unsupported file extension.')

class Album(TimeStampedModel):
    name = models.CharField(default='New Album' , max_length = 80)
    release_datetime = models.DateTimeField(blank = False)
    cost = models.DecimalField(blank = False, decimal_places = 2,max_digits = 15)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    def __str__(self):
        return (f"id: {self.id} \n name: {self.name} cost: {self.cost} \n approved : {self.is_approved}")


class Song(models.Model):
    
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    name = models.CharField(blank = True , max_length = 80 , help_text = "if left empty , will take the name of the album" )
    image =  models.ImageField(blank = False)
    thumbnail = ImageSpecField(format='JPEG')
    # in my opinion , this field will be useful when you want to display 
    # many song images in one page , because fetching all original images will be slower , as it 
    #  has more data , and you don't need the large size , so instead you fetch thumbnails
    # otherwise it will be useless
    audio = models.FileField(blank = False, validators=[validate_file_extension])
    def clean(self):
        if self.name == "":
            self.name = self.album.name

    def delete(self, *args, **kwargs):
        if(self.album.song_set.all().count() >1):
            super(Song, self).delete(*args, **kwargs)
        else:
            raise forms.ValidationError("album has only 1 song , can't be deleted")
