from django.shortcuts import render
from .models import TopSlider, Advantages


def homepage(request):
    sliders = TopSlider.objects.filter(status='published')
    advantages = Advantages.objects.filter(status='published')
    template = 'homepage/homepage.html'
    context = {
        'sliders': sliders,
        'advantages': advantages,
        'title': 'home page'
    }
    return render(request, template, context)
