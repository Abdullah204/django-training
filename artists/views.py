from django.shortcuts import render
from django.views import View

# Create your views here.
from django.http import HttpResponse
from.forms import ArtistForm
from .models import Artist
class CreateView(View):
    template_name = 'createArtist.html'
    def get (self,request,*args, **kwargs):
        form = ArtistForm()
        context = {'form' : form}
        return render(request,self.template_name,context)
    
    def post (self,request,*args, **kwargs):
        form = ArtistForm()
        if(request.method == "POST"):
            form = ArtistForm(request.POST)
            if form.is_valid():
                form.save()
        context = {'form' : form}
        return render(request,self.template_name,context)
    
    
class ListView(View):
    def get(self,request):
        context = {'artist_list' : Artist.objects.prefetch_related('album_set').all()}
        return render(request,'listArtists.html',context)