from django.shortcuts import render, get_object_or_404
from .models import TopSlider, Advantages, GetInspired, TopOffer, Logo, Faq, ContactUsPage, AboutUs
from products.models import Product, Colours, ProductCategory, Brand
from blog.models import Post


def homepage(request):
    contactus = get_object_or_404(ContactUsPage)
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)
    categories= ProductCategory.objects.filter(status='published')
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
        'contactus': contactus,
        'categories': categories
    }
    return render(request, template, context)


def faq(request):
    categories = ProductCategory.objects.filter(status='published')
    contactus = get_object_or_404(ContactUsPage)
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
        'contactus': contactus,
        'categories': categories,
    }
    return render(request, template, context)


def contact(request):
    categories = ProductCategory.objects.filter(status='published')
    contactus = get_object_or_404(ContactUsPage)
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)
    template = 'contact/contact.html'
    context = {
        'logo': logo,
        'offer': offer,
        'contactus': contactus,
        'categories': categories
    }
    return render(request, template, context)


def terms_and_conditions(request):
    categories = ProductCategory.objects.filter(status='published')
    contactus = get_object_or_404(ContactUsPage)
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)
    template = 'pages/terms_and_conditions.html'
    context = {
        'logo': logo,
        'offer': offer,
        'contactus': contactus,
        'categories': categories,
    }
    return render(request, template, context)


def about_us(request):
    categories = ProductCategory.objects.filter(status='published')
    contactus = get_object_or_404(ContactUsPage)
    about_us_data = get_object_or_404(AboutUs)
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)
    template = 'pages/about_us.html'
    context = {
        'logo': logo,
        'offer': offer,
        'about_us_data': about_us_data,
        'contactus': contactus,
        'categories': categories,
    }
    return render(request, template, context)
