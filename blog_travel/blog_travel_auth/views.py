from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from blog_travel_auth.forms import BlogTravelUserCreateForm
from blog_travel_auth.models import BlogTravelUser


class BlogTravelUserCreateView(CreateView):
    model = BlogTravelUser
    success_url = '/'
    form_class = BlogTravelUserCreateForm
