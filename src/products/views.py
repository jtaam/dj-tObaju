from django.shortcuts import render, get_object_or_404
from .models import Brand, ProductCategory, Colours, Product, CategoryGroup
from shophome.models import TopOffer


def products_list(request):
    offer = get_object_or_404(TopOffer)
    brands = Brand.objects.filter(status='published')
    categories = ProductCategory.objects.all()
    colours = Colours.objects.all()
    products = Product.objects.filter(status='published')
    template = 'products/products_list.html'
    context = {
        'offer': offer,
        'products': products,
        'categories': categories,
        'colours': colours,
        'brands': brands,
    }
    return render(request, template, context)


def product_detail(request, pid):
    offer = get_object_or_404(TopOffer)
    brands = Brand.objects.filter(status='published')
    product = get_object_or_404(Product, id=pid)
    colours = Colours.objects.all()
    template = 'products/product_detail.html'
    context = {
        'offer': offer,
        'product': product,
        'brands': brands,
        'colours': colours,
    }
    return render(request, template, context)


def brands_list(request):
    brands = Brand.objects.filter(status='published')
    template = 'products/brand/brands_list.html'
    context = {
        'brands': brands
    }
    return render(request, template, context)


def brand_detail(request, slug):
    brand = get_object_or_404(Brand, slug=slug)
    template = 'products/brand/brand_detail.html'
    context = {
        'brand': brand,
    }
    return render(request, template, context)
