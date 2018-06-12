from django.shortcuts import render, get_object_or_404
from .models import Brand, ProductCategory, Colours, Product, CategoryGroup


def products_list(request):
    men_categories = ProductCategory.objects.all()
    colours = Colours.objects.all()
    products = Product.objects.filter(status='published')
    template = 'products/products_list.html'
    context = {
        'products': products,
        'men_categories': men_categories,
        'colours': colours,
    }
    return render(request, template, context)


def product_detail(request, pid):
    product = get_object_or_404(Product, id=pid)
    template = 'products/product_detail.html'
    context = {
        'product': product
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
