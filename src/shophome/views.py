from django.shortcuts import render, get_object_or_404
from .models import TopSlider, Advantages, GetInspired, TopOffer


def homepage(request):
    offer = get_object_or_404(TopOffer)
    sliders = TopSlider.objects.filter(status='published')
    advantages = Advantages.objects.filter(status='published')
    get_inspired_images = GetInspired.objects.filter(status='published')
    template = 'homepage/homepage.html'
    context = {
        'offer': offer,
        'sliders': sliders,
        'advantages': advantages,
        'inspires': get_inspired_images,
        'title': 'home page'
    }
    return render(request, template, context)
