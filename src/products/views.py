from django.shortcuts import render, get_object_or_404
from .models import Brand, ProductCategory, Colours, Product, CategoryGroup, ProductShareLinks
from shophome.models import TopOffer, Logo, ContactUsPage


def products_list(request):
    contactus = get_object_or_404(ContactUsPage)
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)
    brands = Brand.objects.filter(status='published')
    categories = ProductCategory.objects.filter(status='published')
    colours = Colours.objects.all()
    products = Product.objects.filter(status='published')
    template = 'products/products_list.html'
    context = {
        'offer': offer,
        'products': products,
        'categories': categories,
        'colours': colours,
        'brands': brands,
        'logo': logo,
        'contactus':contactus,
    }
    return render(request, template, context)


def product_detail(request, pid):
    contactus = get_object_or_404(ContactUsPage)
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)
    categories = ProductCategory.objects.filter(status='published')
    brands = Brand.objects.filter(status='published')
    product = get_object_or_404(Product, id=pid)
    products = Product.objects.filter(status='published')[0:3]
    recently_products = Product.objects.filter(status='published')[2:5]
    colours = Colours.objects.all()
    share_links = ProductShareLinks.objects.all()
    template = 'products/product_detail.html'
    context = {
        'offer': offer,
        'product': product,
        'brands': brands,
        'colours': colours,
        'categories': categories,
        'products': products,
        'recently_products': recently_products,
        'logo': logo,
        'share_links': share_links,
        'contactus': contactus,
    }
    return render(request, template, context)


def products_list_by_category(request, category):
    contactus = get_object_or_404(ContactUsPage)
    logo = get_object_or_404(Logo)
    offer = get_object_or_404(TopOffer)
    brands = Brand.objects.filter(status='published')
    categories = ProductCategory.objects.filter(status='published')
    colours = Colours.objects.all()
    products = Product.objects.filter(category=category)
    template = 'products/products_list.html'
    context = {
        'offer': offer,
        'products': products,
        'categories': categories,
        'colours': colours,
        'brands': brands,
        'logo': logo,
        'contactus': contactus,
    }
    return render(request, template, context)


def brands_list(request):
    contactus = get_object_or_404(ContactUsPage)
    logo = get_object_or_404(Logo)
    brands = Brand.objects.filter(status='published')
    template = 'products/brand/brands_list.html'
    context = {
        'brands': brands,
        'logo': logo,
        'contactus': contactus,
    }
    return render(request, template, context)


def brand_detail(request, slug):
    contactus = get_object_or_404(ContactUsPage)
    logo = get_object_or_404(Logo)
    brand = get_object_or_404(Brand, slug=slug)
    template = 'products/brand/brand_detail.html'
    context = {
        'brand': brand,
        'logo': logo,
        'contactus': contactus,
    }
    return render(request, template, context)
