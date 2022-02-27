from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

# from django.views.generic import CreateView
from .models import BlogUser, Profile
from .forms import RegisterForm, LoginForm, EditProfileForm


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


@login_required
def edit_profile(request) -> HttpResponse:
    if request.method == 'POST':
        # user_form = EditUserForm(request.POST, instance=request.user)
        profile = get_object_or_404(Profile, user=request.user)
        profile_form = EditProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            # user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('register:profile', request.user.username)
    else:
        # user_form = EditUserForm(instance=request.user)
        profile_form = EditProfileForm()
        return render(request, 'profile/edit_profile.html', {'profile_form': profile_form})
