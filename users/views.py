from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from authentication.serializers import UserRegistrationSerializer
from users.serializers import UserSerializer
from .models import User
from rest_framework import status

# Create your views here.
class UserDetailView(APIView):

    def get(self, request, pk):
        try:
            user = User.objects.get(pk = pk)
            return Response({
                "id" : user.id,
                'username': user.username,
                'email': user.email,
                'bio' : user.bio
            })            
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    
    def put(self, request, pk):
        if not request.user.pk == pk:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            user = User.objects.get(pk = pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        model_serializer = UserSerializer(user,data=request.data)
        model_serializer.is_valid(raise_exception=True)
        model_serializer.save()
        return Response({
            "id" : user.id,
            'username': user.username,
            'email': user.email,
            'bio' : user.bio
        })



    def patch(self, request, pk):
        if not request.user.pk == pk:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        try:
            user = User.objects.get(pk = pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        model_serializer = UserSerializer(user,data=request.data,partial=True)
        model_serializer.is_valid(raise_exception=True)
        model_serializer.save()
        return Response({
            "id" : user.id,
            'username': user.username,
            'email': user.email,
            'bio' : user.bio
        })             
        

        