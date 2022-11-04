from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views
from albums.views import CreateView
from albums.views import AlbumList , AlbumListManual
urlpatterns = [
    path('create', login_required(CreateView.as_view()), name='create'),
    path('', AlbumList.as_view(), name='album_view'),
    path('manualfilter', AlbumListManual.as_view(), name='album_manual'),
]