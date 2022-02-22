from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView

from blogs.models import Post
#
#
from blogs.forms import PostCreateForm


class HomeView(ListView):
    template_name = 'blogs/index.html'
    queryset = Post.objects.all()
    paginate_by = 5
# def index(request):
#     posts = Post.objects.all()
#     context = {'post_list': reversed(posts)}
#     return render(request, 'blogs/index.html', context=context)

#
# class PostListView(ListView):
#     model = Post


class PostDetailView(DetailView):
    page_title = 'Post Detail'
    model = Post

    # def get_object(self, queryset=None):
    #     return get_object_or_404(Post, slug__iexact=self.kwargs['slug'])
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

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been created successfully.')
        return reverse_lazy("blogs:index")

    def form_valid(self, form):
        print('form:', form)
        form.instance.author = self.request.user
        return super().form_valid(form)

    def save_model(self):
        pass


class PostUpdateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title', 'body', )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        update = True
        context['update'] = update

        return context

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been updated successfully.')
        return reverse_lazy("blogs:index")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)
