from django.contrib import admin
from .models import Artist , Album

# Register your models here.


class AlbumInline(admin.StackedInline):
    model = Album
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('name' , 'creation_datetime' , 'release_datetime' , 'cost' ,'artist'),
            
        }),(None,{
            'fields' : ('approved',),
'description': "Approve the album if its name is not explicit"
        })
    )
    readonly_fields=('creation_datetime',)

class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumInline]

class AlbumAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name' , 'creation_datetime' , 'release_datetime' , 'cost' ,'artist'),
            
        }),(None,{
            'fields' : ('approved',),
'description': "Approve the album if its name is not explicit"
        })
    )
    readonly_fields=('creation_datetime',)


admin.site.register(Artist,ArtistAdmin)
admin.site.register(Album,AlbumAdmin)