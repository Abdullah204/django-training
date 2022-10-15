from django.contrib import admin
from .models import Artist , Album ,Song

# Register your models here.



class SongInline(admin.StackedInline):
    model = Song
    extra = 0
    min_num = 1
class AlbumAdmin(admin.ModelAdmin):
    inlines = [SongInline]
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
admin.site.register(Song)