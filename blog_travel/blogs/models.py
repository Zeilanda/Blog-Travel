from django.db import models

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author_id = models.ForeignKey('User',
                                  on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} <{self.body}>'


class User(models.Model):
    name = models.CharField(max_length=64)
    nickname = models.CharField(max_length=28, db_index=True, unique=True)


class Tag(models.Model):
    name = models.CharField(max_length=28)


