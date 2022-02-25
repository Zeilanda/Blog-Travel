from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

import blogs.views as blogs

# urlpatterns = [
#     path('', blogs.index, name='index')
# ]
import register.views as register

app_name = 'register'

urlpatterns = [
    path('',
         register.signup,
         name='user_create'),
    path('login/',
         register.log_in,
         name='login'),
    path('logout/',
         LogoutView.as_view(),
         name='logout'),
]