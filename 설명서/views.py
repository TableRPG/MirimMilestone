# 설명서/views.py

from django.shortcuts import render, get_object_or_404
from .models import Manual, Category

def category_list(request):
    categories = Category.objects.all()
    return render(request, '설명서/category_list.html', {'categories': categories})

def manual_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    manuals = category.manuals.all()
    return render(request, '설명서/manual_list.html', {'category': category, 'manuals': manuals})

def manual_detail(request, id):
    manual = get_object_or_404(Manual, id=id)
    return render(request, '설명서/manual_detail.html', {'manual': manual})
