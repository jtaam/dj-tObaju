from django.shortcuts import render


def products_list(request):
    template = 'products/products_list.html'
    context = {
        'data': '',
        'title': 'all products',
    }
    return render(request, template, context)
