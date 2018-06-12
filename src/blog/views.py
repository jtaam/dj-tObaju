from django.shortcuts import render, get_object_or_404
from .models import Post
from shophome.models import TopOffer


def blog_list(request):
    offer = get_object_or_404(TopOffer)
    posts = Post.objects.filter(status='published').order_by('-create')
    template = 'blog/blog_list.html'
    context = {
        'offer': offer,
        'posts': posts
    }
    return render(request, template, context)


def blog_detail(request, pid):
    offer = get_object_or_404(TopOffer)
    post = get_object_or_404(Post, id=pid)
    template = 'blog/blog_detail.html'
    context = {
        'offer': offer,
        'post': post
    }
    return render(request, template, context)
