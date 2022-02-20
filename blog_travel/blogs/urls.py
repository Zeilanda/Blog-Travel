
from django.urls import path

import blogs.views as blogs

app_name = 'blogs'

urlpatterns = [
    path('', blogs.index, name='index'),
]
