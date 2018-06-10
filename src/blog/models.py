from django.db import models


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


class Post(models.Model):
    CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(250)
    subtitle = models.TextField(blank=True, null=True)
    description = models.TextField()
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/post/%Y/%m/%d/')
    status = models.CharField(choices=CHOICES, max_length=20)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
