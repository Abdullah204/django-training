from django.contrib import admin
from users.forms import UserRegisterForm
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django import forms
from django.contrib.auth import password_validation


# Register your models here.
class UserRegisterAdminForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    bio = forms.CharField( widget=forms.Textarea , required= False)
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password','bio']
    def clean_password(self):
        pw = self.cleaned_data['password']
        password_validation.MinimumLengthValidator().validate(pw)
        password_validation.CommonPasswordValidator().validate(pw)
        password_validation.NumericPasswordValidator().validate(pw)
        password_validation.UserAttributeSimilarityValidator().validate(pw)

class UserRegisterAdmin(admin.ModelAdmin):
    fields = ['username' , 'email' , 'password','bio']
    form = UserRegisterAdminForm
admin.site.register(User, UserRegisterAdmin)
