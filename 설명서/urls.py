# 설명서/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('category/<int:category_id>/', views.manual_list, name='manual_list_by_category'),
    path('설명서/<int:id>/', views.manual_detail, name='manual_detail'),
]
