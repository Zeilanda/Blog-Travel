from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404

from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import BlogUser, Profile
from .forms import RegisterForm, LoginForm


def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blogs:index')
    else:
        form = UserCreationForm()
    return render(request, 'register/bloguser_form.html', {'form': form})


def log_in(request):
    if request.user.is_authenticated:
        return redirect('blogs:index')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('blogs:index')
            else:
                messages.error(request, 'Неправильный email или пароль')

    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})


@login_required
def profile(request, username):
    user = get_object_or_404(BlogUser, username=username)
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'profile/profile.html', {'profile': profile, 'user': user})

