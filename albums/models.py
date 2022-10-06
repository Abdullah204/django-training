from unicodedata import decimal
from django.db import models
import datetime
from django.utils import timezone
from artists.models import Artist

class Album(models.Model):
    name = models.CharField(default='New Album' , max_length = 80)
    creation_datetime = models.DateTimeField(default=timezone.now ,editable=False)
    release_datetime = models.DateTimeField(blank = False)
    cost = models.DecimalField(blank = False, decimal_places = 2,max_digits = 15)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    def __str__(self):
        return (f"{self.id} {self.name}")

    

