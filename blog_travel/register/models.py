from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.


class BlogUser(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    d_birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True)
