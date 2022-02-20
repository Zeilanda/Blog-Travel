# from django.contrib.auth.models import User
from django.db import models

from django.db import models

from register.models import BlogUser


class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(BlogUser,
                               on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} <{self.body}>'


#
# class Person(models.Model):
#     user = models.OneToOneField(
#         User,
#         on_delete=models.CASCADE,
#         primary_key=True
#     )
#     birthdate = models.DateField(blank=True, null=True)
#     email = models.EmailField()
#     nickname = models.TextField()



#
# class Tag(models.Model):
#     name = models.CharField(max_length=28)
