# from django.contrib.auth.models import User

from django.db import models
<<<<<<< Updated upstream
from django.utils.timezone import now
=======
from django.utils import timezone
>>>>>>> Stashed changes

from register.models import BlogUser


class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(BlogUser,
                               on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return f'{self.title} <{self.body}>'

<<<<<<< Updated upstream
=======

print(timezone.now())

>>>>>>> Stashed changes

class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name='comments')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment on {}'.format(self.post)
