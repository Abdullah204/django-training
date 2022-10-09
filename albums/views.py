from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from.forms import AlbumForm

def create(request):
    form = AlbumForm()
    if(request.method == "POST"):
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form' : form}
    return render(request,'createAlbum.html',context)

