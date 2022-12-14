from django.db import models
from django.contrib import admin
from musicplatform import settings
# Create your models here.
class Artist(models.Model):
    stage_name = models.CharField(blank = False,unique=True , max_length = 80)
    social_link_field = models.URLField(blank = True , null = False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key = True
    )
    class Meta:
        ordering = ('stage_name',)
    def __str__(self):
        approved_albums = self.album_set.filter(is_approved__exact =True).count()
        return (f"name: {self.stage_name} \n social_url: {self.social_link_field} \n  {approved_albums} approved albums")
    def approved_albums(self):
        return self.album_set.filter(is_approved=True).count()
