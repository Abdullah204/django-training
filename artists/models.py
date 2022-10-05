from django.db import models

# Create your models here.
class Artist(models.Model):
    stage_name = models.CharField(blank = False,unique=True , max_length = 80)
    social_link_field = models.URLField(blank = True , null = False)
    class Meta:
        ordering = ('stage_name',)
    def __str__(self):
        return (f"{self.stage_name} {self.social_link_field}")