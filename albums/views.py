from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from artists.models import Artist
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .filters import AlbumFilter
from django.http import HttpResponse
from.forms import AlbumForm
from django.views import View
from rest_framework.views import APIView
from albums.models import Album
from albums.serializers import AlbumSerializer
class CreateView(View):
    template_name = 'createAlbum.html'

    def get(self, request, *args, **kwargs):
        form = AlbumForm()
        context = {'form' : form}
        return render(request,self.template_name,context)
    
    def post(self, request, *args, **kwargs):
        form = AlbumForm()
        if(request.method == "POST"):
            form = AlbumForm(request.POST)
            if form.is_valid():
                form.save()
        context = {'form' : form}
        return render(request,self.template_name,context)



  

class AlbumList(APIView):
    """
    List all APPROVED albums, or create a new album.
    """
    pagination_class = LimitOffsetPagination
    permission_classes = IsAuthenticatedOrReadOnly
    filterset_class = AlbumFilter
    filter_backends = (filters.DjangoFilterBackend,)


    def get(self, request, format=None):
        albums = Album.objects.filter(is_approved=True).all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        id = request.user.id
        try :
            artist = Artist.objects.get(id=id)
        except :
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():

            model_obj = serializer.save()
            model_obj.artist = artist
            model_obj.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


