from django.db import models
from django.conf import settings


class PostCategory(models.Model):
    CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/category/%Y/%m/%d/')
    status = models.CharField(choices=CHOICES, max_length=20)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Post Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    subtitle = models.TextField(blank=True, null=True)
    description = models.TextField()
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    image = models.ImageField(upload_to='blog/post/%Y/%m/%d/')
    status = models.CharField(choices=CHOICES, max_length=20)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
