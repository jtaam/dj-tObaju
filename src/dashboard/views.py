from django.shortcuts import render


def dashboard(request):
    template = 'dashboard/index.html'
    context = {}
    return render(request, template, context)


def add_blog_category(request):
    template = 'dashboard/blog/category/add-category.html'
    context = {}
    return render(request, template, context)


def blog_categories(request):
    template = 'dashboard/blog/category/categories.html'
    context = {}
    return render(request, template, context)


def add_post(request):
    template = 'dashboard/blog/post/add-post.html'
    context = {}
    return render(request, template, context)


def posts_list(request):
    template = 'dashboard/blog/post/posts-list.html'
    context = {}
    return render(request, template, context)