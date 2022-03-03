from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from blogs.models import Post, Comment
#
#
from blogs.forms import PostCreateForm, PostUpdateForm, CommentCreateForm
from register.models import BlogUser


class HomeView(ListView):
    template_name = 'blogs/index.html'
    queryset = Post.objects.all()
    paginate_by = 5

def TagView(request, ):
    tag_posts = Post.objects.filter(tags=)
    return render(request, 'blogs/chosen_tags.html', {})


class PostDetailView(DetailView):
    page_title = 'Post Detail'
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    page_title = 'Post Create'
    model = Post

    form_class = PostCreateForm
    success_url = 'blogs:index'

    def get_form_class(self):
        res = super().get_form_class()
        return res

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been created successfully.')
        return reverse_lazy("blogs:index")

    def form_valid(self, form):
        # print('form:', form)
        form.instance.author = self.request.user
        result = super().form_valid(form)
        # form.instance.tags.set([])
        return result

    def get_queryset(self):
        # print('get_queryset')
        return super().get_queryset()


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = 'blogs/update_post.html'
    # fields = ['title', 'body', 'tags']

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been updated successfully.')
        return reverse_lazy("blogs:post_detail", kwargs={'pk': self.kwargs['pk']})

    def get_queryset(self):
        # print('get_queryset')
        res = super().get_queryset()
        # print(res)
        return res


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blogs/delete_post.html'

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been deleted successfully.')
        return reverse_lazy("blogs:index")

    # def get_queryset(self):
    #     return self.model.objects.filter(author=self.request.user)


class CommentCreateView(CreateView):
    model = Comment
    template_name = 'blogs/add_comment.html'
    # fields = '__all__'
    form_class = CommentCreateForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        result = super().form_valid(form)
        # form.instance.tags.set([])
        return result

    def get_success_url(self):
        messages.success(
            self.request, 'Your post has been deleted successfully.')
        return reverse_lazy('blogs:post_detail', kwargs={'pk': self.kwargs['pk']})
