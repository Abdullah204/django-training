from urllib import request
from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
# Create your models here.
class User(AbstractUser):
    bio = models.CharField(max_length =256 , blank = True)
