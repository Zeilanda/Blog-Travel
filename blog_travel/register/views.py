from django.shortcuts import render

from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import BlogUser
from .forms import RegisterForm


# Create your views here.
# def register(response):
#     if response.method == "POST":
#         form = RegisterForm(response.POST)
#         if form.is_valid():
#             form.save()
#
#             return redirect("/home")
#     else:
#         form = RegisterForm()
#
#     return render(response, "register/bloguser_form.html", {"form": form})

class BlogUserCreateView(CreateView):
    model = BlogUser
    success_url = '/'
    form_class = RegisterForm
