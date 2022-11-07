from django.shortcuts import render
from django.views import View

# Create your views here.
from artists.models import Artist
from artists.serializers import ArtistSerializer ,ArtistRequestSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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





class ArtistList(APIView):
    """
    List all artists, or create a new artist.
    """
    def get(self, request, format=None):
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArtistSerializer(data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)