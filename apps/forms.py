from django.contrib.auth.models import User
from django.contrib.auth.forms import  UserCreationForm
from django import forms


class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email', 'password1', 'password2']

class Login(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

