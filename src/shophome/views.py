from django.shortcuts import render


def homepage(request):
    template = 'homepage/homepage.html'
    context = {
        'data': '',
        'title': 'home page'
    }
    return render(request, template, context)
