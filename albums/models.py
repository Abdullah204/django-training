from unicodedata import decimal
from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
from artists.models import Artist
class Album(models.Model):
    name = models.CharField(default='New Album' , max_length = 80)
    creation_datetime = models.DateTimeField(default=timezone.now)
    release_datetime = models.DateTimeField(blank = False)
    cost = models.DecimalField(blank = False, decimal_places = 2,max_digits = 15)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    def __str__(self):
        return (f"{self.id} {self.name}")

    

# album2 = Album(name="album2" , release_datetime =datetime.datetime(2014, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC),cost=15.5)