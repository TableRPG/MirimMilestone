# 설명서/models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Manual(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    category = models.ForeignKey(Category, related_name='manuals', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='manual_images/', null=True, blank=True)

    def __str__(self):
        return self.title
