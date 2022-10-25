from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

# Create your views here.
class UserDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        pk = self.kwargs['pk']
        return 

    def post(self, request, format=None):
        return 
    
    def put(self, request, format=None):
        return 