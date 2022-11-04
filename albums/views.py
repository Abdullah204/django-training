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
from django import forms
from albums.serializers import AlbumSerializer , AlbumRequestSerializer
import sys
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
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = AlbumFilter
    filter_backends = (filters.DjangoFilterBackend,)


    def get(self, request, format=None):
        albums = Album.objects.filter(is_approved=True).all()
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        try :
            artist = Artist.objects.get(user = request.user)
        except :
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = AlbumRequestSerializer(data=request.data ,context={'artist': artist})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumListManual(APIView):
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        lte = request.query_params.get('lte')
        gte = request.query_params.get('gte')
        name = request.query_params.get('name')
        try:
            if(not lte is None):
                lte = int(lte)
        except:
            raise forms.ValidationError("incorrect data type for lte")
        try:
            if(not gte is None):
                gte = int(gte)
        except:
            raise forms.ValidationError("incorrect data type for gte")
        
        if(not gte is None and not lte is None and not name is None):
            albums = Album.objects.filter(cost__lte = lte , cost__gte = gte ,name__iexact= name).all()
        elif(not gte is None and not lte in None):
            albums = Album.objects.filter(cost__lte = lte , cost__gte = gte).all()
        elif(not gte is None and not name in None):
            albums = Album.objects.filter(name__iexact= name , cost__gte = gte).all()
        elif(not lte is None and not name in None):
            albums = Album.objects.filter( name__iexact= name , cost__lte = lte).all()
        elif(not lte is None):
            albums = Album.objects.filter( cost__lte = lte).all()
        elif(not gte is None):
            albums = Album.objects.filter(cost__gte = gte).all()
        elif(not name is None):
            albums = Album.objects.filter(name__iexact= name ).all()
        else:
            albums = Album.objects.all()
        albums = albums.filter(is_approved = True)
        serializer = AlbumSerializer(albums, many=True)
        return Response(serializer.data)