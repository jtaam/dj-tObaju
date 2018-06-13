from django.shortcuts import render


def dashboard(request):
    template = 'dashboard/index.html'
    context = {}
    return render(request, template, context)
