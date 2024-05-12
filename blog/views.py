
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post

from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin, UserPassesTestMixin
)
from django.core.exceptions import PermissionDenied
from django.contrib.auth.views import redirect_to_login

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/home.html'
    ordering = '-date_posted'
    paginate_by = 2

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    context_object_name = 'form'
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    context_object_name = 'form'
    template_name = 'blog/post_form.html'
    success_url = '/'
    login_url = '/user/login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())

        return redirect_to_login(
            self.request.get_full_path(),
            self.get_login_url(),
            self.get_redirect_field_name()
        )


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    context_object_name = 'object'
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'
    login_url = '/user/login'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())

        return redirect_to_login(
            self.request.get_full_path(),
            self.get_login_url(),
            self.get_redirect_field_name()
        )

class UserPostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/user_posts.html'
    ordering = '-date_posted'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user)


def latest_articles_view(request):
    posts = Post.objects.all().order_by('-date_posted')[:3]
    context = {
        'posts' : posts
    }
    return render(request,'blog/latest_posts.html', context)


def responsive_view(request):
    return render(request, 'blog/responsive.html')


def top_interview_questions_view(request):
    return render(request, 'blog/interview_questions.html')

'''
def home_view(request):
    posts = Post.objects.all().order_by('-date_posted')
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html', context)
'''


