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
         register.BlogUserCreateView.as_view(),
         name='user_create'),
    path('login/',
         LoginView.as_view(),
         name='login'),
    path('logout/',
         LogoutView.as_view(),
         name='logout'),
]