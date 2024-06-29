from django.shortcuts import render
from django.views.generic import TemplateView

from 게시판.models import Post
from 설명서.models import Category

class HomeView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_list'] = Post.objects.order_by('-created_at')[:3]  # 최근거 3개만 추가
        context['categories'] = Category.objects.all()  # 모든 카테고리를 컨텍스트에 추가
        return context
