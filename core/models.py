


from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django_summernote.fields import SummernoteTextField


# Create your models here.

STATUS = [
    ('Draft', 'Draft'),
    ('Published', 'Published')
]


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tags')

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    insight = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=15, choices=STATUS, default='Draft')
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)

    class Meta:
        ordering = [
            '-publish'
        ]

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = [
            '-created'
        ]

    def __str__(self):
        return f'Comment by {self.name} on {self.post.title}'



class Message(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField()
