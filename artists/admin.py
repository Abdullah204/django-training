from atexit import register
from django.contrib import admin
from .models import Artist 
# Register your models here.
class ArtistAdmin(admin.ModelAdmin):
    list_display = ["stage_name", "social_link_field", "approved_albums"]
admin.site.register(Artist,ArtistAdmin)
