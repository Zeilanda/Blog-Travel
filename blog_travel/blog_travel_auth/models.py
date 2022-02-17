from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class BlogTravelUser(AbstractUser):
    email = models.EmailField('email address', unique=True)
    d_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True)
