from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView

from blogs.models import Post
#
#
from blogs.forms import PostCreateForm


def index(request):
    posts = Post.objects.all()
    context = {'post_list': reversed(posts)}
    return render(request, 'blogs/index.html', context=context)


class PostListView(ListView):
    model = Post

# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()
#
#     return render(request, 'blogs/name.html', {'form': form})


class PostCreateView(LoginRequiredMixin, CreateView):
    page_title = 'Post Create'
    model = Post
    # form_class = PostCreateForm
    success_url = '/'
    fields = ('title', 'body', )

    def form_valid(self, form):
        print('form:', form)
        form.instance.author = self.request.user
        return super().form_valid(form)
    #
    # @method_decorator(login_required())
    # def dispatch(self, request, *args, **kwargs):
    #
    #     current_user = request.user
    #     kwargs['current_user'] = current_user.id
    #     print(current_user.id)
    #     # print(request)
    #     # print(args)
    #     # print(kwargs)
    #     return super().dispatch(request, *args, **kwargs)

    def save_model(self):
        pass