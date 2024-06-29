from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'ip', 'created_at')

    def save_model(self, request, obj, form, change):
        if not obj.ip:
            obj.ip = self.get_client_ip(request)
        obj.save()

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user_name', 'reply')

    def save_model(self, request, obj, form, change):
        if not obj.ip:
            obj.ip = self.get_client_ip(request)
        obj.save()

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
