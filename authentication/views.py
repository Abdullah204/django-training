from .serializers import UserRegistrationSerializer
from users.serializers import UserSerializer
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import  login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

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

class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        sup = super(LoginView, self).post(request, format=None)
        return Response({
            'token': sup.data['token'],
            'username': user.username,
            'email': user.email,
            'bio' : user.bio
        })

