from django.urls import path

from 게시판 import views

app_name='게시판'

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
    path('<int:post_id>/comment', views.CommentCreate.as_view(), name='comment_create')
]