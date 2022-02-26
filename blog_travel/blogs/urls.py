from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
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
    path('profile/<username>/', profile, name='profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

