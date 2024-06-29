from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1500)
    ip = models.GenericIPAddressField(null=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " " + self.content

    def get_absolute_url(self):
        return reverse('게시판:post_detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    reply = models.TextField(max_length=500)
    ip = models.GenericIPAddressField(null=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=55, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.user_name:
            if self.ip == self.post.ip:
                self.user_name = '🙋작성자🙋‍♂️'
            else:
                existing_comments_count = Comment.objects.filter(post=self.post).count()
                self.user_name = f'미림인_{existing_comments_count + 1}'
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.post) + " : " + self.reply