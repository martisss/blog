from django.db import models
from django.contrib.auth.models import User
from blog.models import Article


# Create your models here.

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments',verbose_name="文章")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments',verbose_name='用户')
    body = models.TextField(verbose_name='评论内容')
    created = models.DateTimeField(auto_now_add=True, verbose_name='评论创建时间')

    class Meta:
        ordering = ('created',)
        verbose_name = '评论'
        verbose_name_plural = '评论'

    def __str__(self):
        return self.body[:20]
