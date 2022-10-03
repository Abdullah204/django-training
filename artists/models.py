from django.db import models

# Create your models here.
class Artist(models.Model):
    stage_name = models.CharField(required = True,unique=True)
    social_link_field = models.URLField(null = False, blank = False)
