from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=256)


class Comment(models.Model):
    content = models.CharField(max_length=256)
    author = models.CharField(max_length=32)
    post = models.ForeignKey(
        Post,
        related_name='comments',
        on_delete=models.CASCADE
    )
