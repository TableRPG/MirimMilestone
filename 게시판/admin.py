from django.contrib import admin

from 게시판.models import Post, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)