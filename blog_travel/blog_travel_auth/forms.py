from django.contrib.auth.forms import UserCreationForm

from blog_travel_auth.models import BlogTravelUser


class BlogTravelUserCreateForm(UserCreationForm):

    class Meta:
        model = BlogTravelUser
        fields = ('username', 'email', 'password1', 'password2')
