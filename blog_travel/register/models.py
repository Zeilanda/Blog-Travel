from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.


class BlogUser(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Profile(models.Model):
    user = models.OneToOneField(BlogUser, on_delete=models.CASCADE)

    bio = models.TextField()

    def __str__(self):
        return self.user.username
