from django.urls import path

from 게시판 import views

urlpatterns = [
    path('', views.PostList.as_view(), name='post_list'),
    path('<int:id>/', views.PostDetail.as_view(), name='post_detail'),
    path('create/', views.PostCreate.as_view(), name='post_create'),
]