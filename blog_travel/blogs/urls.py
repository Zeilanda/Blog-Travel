
from django.urls import path

import blogs.views as blogs

urlpatterns = [
    path('', blogs.index, name='index')
]
