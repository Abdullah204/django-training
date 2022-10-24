from users.models import User
from .serializers import UserRegistrationSerializer
from users.serializers import UserSerializer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render
from rest_framework import permissions
from django.http import HttpResponse
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from django import forms
from rest_framework.generics import CreateAPIView



class AdminOrGuest(permissions.BasePermission):
     def has_permission(self, request, view):        
        return request.user.is_anonymous or request.user.is_superuser

   



class RegisterView(APIView):
    permission_classes = [AdminOrGuest]

    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Everything's valid, so send it to the UserSerializer
        model_serializer = UserSerializer(data=serializer.data)
        model_serializer.is_valid(raise_exception=True)
        model_serializer.save()

        return Response(model_serializer.data)

# class CreateUserView(CreateAPIView):
#     model = User.objects.all()
#     permission_classes = [AdminOrGuest]
#     serializer_class = UserSerializer



