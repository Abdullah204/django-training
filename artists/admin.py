from django.contrib import admin
from .models import Artist 
from albums.admin import AlbumInline
# Register your models here.
class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumInline]
    list_display = ["stage_name", "social_link_field", "approved_albums"]
admin.site.register(Artist,ArtistAdmin)
