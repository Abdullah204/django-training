from django.forms import ModelForm
from django import forms
from users.models import User
class UserRegisterForm (ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password','confirm_password','bio']
    def clean_password(self):
        pw1 = self.cleaned_data.get('password')
        pw2 = self.data.get('confirm_password')
        if not pw1:
            raise forms.ValidationError("You must enter a password")
        if not pw2:
            raise forms.ValidationError("You must confirm your password")
        if pw1 != pw2:
            raise forms.ValidationError("Your passwords do not match")
        return pw1