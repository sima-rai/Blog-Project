from django import forms
from django.contrib.auth.models import User
from .models import *



class SignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())



class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "image", "content"]
        
