from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from register.models import BlogUser


class RegisterForm(UserCreationForm):
    # email = forms.EmailField()

    class Meta:
        model = BlogUser
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_obj in self.fields.items():
            field_obj.help_text = '\n'
            print(field_name, field_obj.help_text)
