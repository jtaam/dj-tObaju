from django.shortcuts import render
from .models import TopSlider, Advantages, GetInspired


def homepage(request):
    sliders = TopSlider.objects.filter(status='published')
    advantages = Advantages.objects.filter(status='published')
    get_inspired_images = GetInspired.objects.filter(status='published')
    template = 'homepage/homepage.html'
    context = {
        'sliders': sliders,
        'advantages': advantages,
        'inspires': get_inspired_images,
        'title': 'home page'
    }
    return render(request, template, context)
