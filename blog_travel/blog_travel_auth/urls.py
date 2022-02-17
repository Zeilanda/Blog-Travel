from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

import blog_travel_auth.views as blog_travel_auth


urlpatterns = [
    path('user/create/',
         blog_travel_auth.BlogTravelUserCreateView.as_view(),
         name='user_create'),
    path('login/',
         LoginView.as_view(),
         name='login'),
    path('logout/',
         LogoutView.as_view(),
         name='logout'),
]
