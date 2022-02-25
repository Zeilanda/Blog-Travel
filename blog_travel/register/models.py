from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.


class BlogUser(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Profile(models.Model):
    bio = models.TextField(blank=True)
    d_birth = models.DateField(blank=True, null=True)
    user = models.OneToOneField(BlogUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
