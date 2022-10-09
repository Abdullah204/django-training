from django.contrib import admin
from .models import Artist , Album

# Register your models here.


class AlbumInline(admin.StackedInline):
    model = Album
    extra = 1
    fieldsets = (
        (None, {
            'fields': ('name' , 'created' , 'release_datetime' , 'cost' ,'artist'),
            
        }),(None,{
            'fields' : ('is_approved',),
'description': "Approve the album if its name is not explicit"
        })
    )
    readonly_fields=('created',)



class AlbumAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name' , 'created' , 'release_datetime' , 'cost' ,'artist'),
            
        }),(None,{
            'fields' : ('is_approved',),
'description': "Approve the album if its name is not explicit"
        })
    )
    readonly_fields=('created',)


admin.site.register(Album,AlbumAdmin)