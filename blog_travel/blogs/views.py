from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView

# from blogs.models import Post
#
#
from blogs.forms import NameForm


def index(request):

    return render(request, 'blogs/index.html')
    # posts = Post.objects.all()
    # context = {'post_list': posts}


# class PostListView(ListView):
#     model = Post

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'blogs/name.html', {'form': form})
