from django.shortcuts import render, get_object_or_404
from .models import Brand, ProductCategory, Colours, Product


def products_list(request):
    template = 'products/products_list.html'
    context = {
        'data': '',
        'title': 'all products',
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
