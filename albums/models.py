from unicodedata import decimal
from django.db import models
import datetime
from django.utils import timezone
from artists.models import Artist
from model_utils.models import TimeStampedModel
class Album(TimeStampedModel):
    name = models.CharField(default='New Album' , max_length = 80)
    release_datetime = models.DateTimeField(blank = False)
    cost = models.DecimalField(blank = False, decimal_places = 2,max_digits = 15)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)
    def __str__(self):
        return (f"id: {self.id} \n name: {self.name} cost: {self.cost} \n approved : {self.is_approved}")


