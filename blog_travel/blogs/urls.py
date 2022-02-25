from django.conf.urls import url
from django.urls import path

import blogs.views as blogs
from register.views import profile

app_name = 'blogs'

urlpatterns = [
    path('',
         blogs.HomeView.as_view(),
         name='index'),
    path('create/',
         blogs.PostCreateView.as_view(),
         name='post_create'),
    path('<int:pk>/',
         blogs.PostDetailView.as_view(),
         name='post_detail'),
    # path('profile/<username>/', profile, name='profile')
    # path(r'^about_me/',
    #      blogs.get_user_profile,
    #      name='about_me'),
#     path('profile/<int:pk>/',
#          blogs.get_user_profile,
#          name='about_me'),
]
