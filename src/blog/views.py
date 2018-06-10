from django.shortcuts import render, get_object_or_404


def blog_list(request):
    template = 'blog/blog_list.html'
    context = {
        'posts': 'posts'
    }
    return render(request, template, context)
