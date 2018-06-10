from django.shortcuts import render, get_object_or_404
from .models import Post


def blog_list(request):
    posts = Post.objects.filter(status='published').order_by('-create')
    template = 'blog/blog_list.html'
    context = {
        'posts': posts
    }
    return render(request, template, context)
