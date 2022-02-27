from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from blogs.models import Post
#
#
from blogs.forms import PostCreateForm
from register.models import BlogUser


class HomeView(ListView):
    template_name = 'blogs/index.html'
    queryset = Post.objects.all()
    paginate_by = 5


class PostDetailView(DetailView):
    page_title = 'Post Detail'
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    page_title = 'Post Create'
    model = Post
    # form_class = PostCreateForm
    success_url = 'blogs:index'
    fields = ('title', 'body', 'tags')

    def get_form_class(self):
        print('testing tags', self.fields, self.model)
        res= super().get_form_class()
        print('done')
        return res


    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been created successfully.')
        return reverse_lazy("blogs:index")

    def form_valid(self, form):
        print('form:', form)
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def save_model(self):
    #     pass


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ('title', 'body', 'tags')

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


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been deleted successfully.')
        return reverse_lazy("core:home")

    def get_queryset(self):
        return self.model.objects.filter(author=self.request.user)
