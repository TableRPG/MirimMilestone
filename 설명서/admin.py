# 설명서/admin.py

from django.contrib import admin
from .models import Manual, Category

admin.site.register(Manual)
admin.site.register(Category)
