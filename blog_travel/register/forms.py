from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from register.models import BlogUser, Profile


class RegisterForm(UserCreationForm):
    # email = forms.EmailField()

    class Meta:
        model = BlogUser
        fields = ("username", 'email')


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()


# class EditUserForm(forms.ModelForm):
#     username = forms.CharField(max_length=100,
#                                required=True,
#                                widget=forms.TextInput(attrs={'class': 'form-control'}))
#     email = forms.EmailField(required=True,
#                              widget=forms.TextInput(attrs={'class': 'form-control'}))
#
#     class Meta:
#         model = BlogUser
#         fields = ['username', 'email']


class EditProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), required=False)

    class Meta:
        model = Profile
        fields = ['bio', ]
