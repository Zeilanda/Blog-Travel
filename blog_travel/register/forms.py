from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from register.models import BlogUser


class RegisterForm(UserCreationForm):
    # email = forms.EmailField()

    class Meta:
        model = BlogUser
        fields = ("username", 'email')


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()
