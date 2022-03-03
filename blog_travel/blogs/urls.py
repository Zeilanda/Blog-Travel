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
    path('profile/<username>/', profile, name='profile'),
    path('<int:pk>/edit/',
         blogs.PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete/',
         blogs.PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/comment/',
         blogs.CommentCreateView.as_view(), name='comment_create'),
    path('tag/<slug>/', blogs.tag, name='tag_view')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

