from django.shortcuts import render, get_object_or_404
from .models import Post
from shophome.models import TopOffer, Logo, ContactUsPage
from products.models import ProductCategory


def blog_list(request):
    categories = ProductCategory.objects.filter(status='published')
    contactus = get_object_or_404(ContactUsPage)
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)
    posts = Post.objects.filter(status='published').order_by('-create')
    template = 'blog/blog_list.html'
    context = {
        'offer': offer,
        'posts': posts,
        'logo': logo,
        'contactus': contactus,
        'categories': categories,
    }
    return render(request, template, context)


def blog_detail(request, pid):
    categories = ProductCategory.objects.filter(status='published')
    contactus = get_object_or_404(ContactUsPage)
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)
    post = get_object_or_404(Post, id=pid)
    template = 'blog/blog_detail.html'
    context = {
        'offer': offer,
        'post': post,
        'logo': logo,
        'contactus': contactus,
        'categories': categories,
    }
    return render(request, template, context)
