
from django.urls import path

import blogs.views as blogs

app_name = 'blogs'

urlpatterns = [
    path('',
         blogs.HomeView.as_view(),
         name='index'),
    path('create/',
         blogs.PostCreateView.as_view(),
         name='post_create'),
    path('<int:pk>/', blogs.PostDetailView.as_view(),
         name='post_detail')
]
