from django.db import models
from django.contrib import admin

# Create your models here.
class Artist(models.Model):
    stage_name = models.CharField(blank = False,unique=True , max_length = 80)
    social_link_field = models.URLField(blank = True , null = False)
    class Meta:
        ordering = ('stage_name',)
    def __str__(self):
        approved_albums = self.album_set.filter(approved__exact =True).count()
        return (f"name: {self.stage_name} \nsocial_url: {self.social_link_field}\n  {approved_albums} approved albums")

