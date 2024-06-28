from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, __all__

from 게시판.models import Post


# Create your views here.

class PostList(ListView):
    model = Post
    template_name = 'post/post_list.html'

class PostDetail(DetailView):
    model = Post

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('post:post_list')

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