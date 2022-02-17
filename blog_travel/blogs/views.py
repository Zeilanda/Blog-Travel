from django.shortcuts import render

from django.http import HttpResponse
from django.views.generic import ListView

from blogs.models import Post


def index(request):
    posts = Post.objects.all()
    context = {'post_list': posts}
    return render(request, 'blogs/index.html', context=context)


class PostListView(ListView):
    model = Post
