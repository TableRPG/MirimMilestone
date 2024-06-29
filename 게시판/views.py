from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, __all__

from 게시판.models import Post, Comment


# Create your views here.

class PostList(ListView):
    model = Post
    template_name = 'post/post_list.html'
    ordering = ['-created_at']

class PostDetail(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.object)
        return context

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name_suffix = '_create'
    template_name = 'post/post_create.html'
    success_url = reverse_lazy('게시판:post_list')

    def form_valid(self, form):
        form.instance.ip = self.get_client_ip()
        return super().form_valid(form)

    def get_client_ip(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip

class CommentCreate(CreateView):
    model = Comment
    fields = ['reply']
    template_name_suffix = '_create'
    template_name = 'post/comment_create.html'

    def form_valid(self, form):
        form.instance.ip = self.get_client_ip()
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return super().form_valid(form)

    def get_client_ip(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        return ip

    def get_success_url(self):
        return self.object.post.get_absolute_url()
