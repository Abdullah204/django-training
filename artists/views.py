from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from.forms import ArtistForm
from .models import Artist
def create(request):
    form = ArtistForm()
    if(request.method == "POST"):
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form' : form}
    return render(request,'createArtist.html',context)
def list(request):
    context = {'artist_list' : Artist.objects.prefetch_related('album_set').all()}
    return render(request,'listArtists.html',context)