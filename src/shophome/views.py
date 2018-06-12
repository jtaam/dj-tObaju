from django.shortcuts import render, get_object_or_404
from .models import TopSlider, Advantages, GetInspired, TopOffer
from products.models import Product
from blog.models import Post


def homepage(request):
    offer = get_object_or_404(TopOffer)
    sliders = TopSlider.objects.filter(status='published')
    advantages = Advantages.objects.filter(status='published')
    products = Product.objects.filter(status='published')
    get_inspired_images = GetInspired.objects.filter(status='published')
    posts = Post.objects.filter(status='published')[0:2]
    template = 'homepage/homepage.html'
    context = {
        'offer': offer,
        'sliders': sliders,
        'advantages': advantages,
        'products': products,
        'inspires': get_inspired_images,
        'posts': posts,
        'title': 'home page',
    }
    return render(request, template, context)
