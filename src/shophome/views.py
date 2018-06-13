from django.shortcuts import render, get_object_or_404
from .models import TopSlider, Advantages, GetInspired, TopOffer, Logo, Faq, ContactUsPage
from products.models import Product, Colours, ProductCategory, Brand
from blog.models import Post


def homepage(request):
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)
    sliders = TopSlider.objects.filter(status='published')
    advantages = Advantages.objects.filter(status='published')
    products = Product.objects.filter(status='published')
    get_inspired_images = GetInspired.objects.filter(status='published')
    posts = Post.objects.filter(status='published')[0:2]
    template = 'homepage/homepage.html'
    context = {
        'logo': logo,
        'offer': offer,
        'sliders': sliders,
        'advantages': advantages,
        'products': products,
        'inspires': get_inspired_images,
        'posts': posts,
        'title': 'home page',
    }
    return render(request, template, context)


def faq(request):
    faqs = Faq.objects.filter(status='published')
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)
    categories = ProductCategory.objects.filter(status='published')
    colours = Colours.objects.all()
    brands = Brand.objects.filter(status='published')
    template = 'pages/faq.html'
    context = {
        'faqs': faqs,
        'logo': logo,
        'offer': offer,
        'categories': categories,
        'colours': colours,
        'brands': brands,
    }
    return render(request, template, context)


def contact(request):
    contactus = get_object_or_404(ContactUsPage)
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)
    template = 'contact/contact.html'
    context = {
        'logo': logo,
        'offer': offer,
        'contactus': contactus,
    }
    return render(request, template, context)


def terms_and_conditions(request):
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)
    template = 'pages/terms_and_conditions.html'
    context = {
        'logo': logo,
        'offer': offer,
    }
    return render(request, template, context)


def about_us(request):
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)
    template = 'pages/about_us.html'
    context = {
        'logo': logo,
        'offer': offer,
    }
    return render(request, template, context)
