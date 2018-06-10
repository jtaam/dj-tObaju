from django.shortcuts import render
from .models import TopSlider


def homepage(request):
    sliders = TopSlider.objects.filter(status='published')
    template = 'homepage/homepage.html'
    context = {
        'sliders': sliders,
        'title': 'home page'
    }
    return render(request, template, context)
