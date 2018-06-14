from django.contrib import messages
from django.shortcuts import render, redirect
from blog.models import PostCategory, Post
from .forms import PostCategoryForm


def dashboard(request):
    template = 'dashboard/index.html'
    context = {}
    return render(request, template, context)


def add_blog_category(request):
    form = PostCategoryForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.info(request, 'Successfully created a new blog category.')
        return redirect('/dashboard/blog_categories/')
    template = 'dashboard/blog/category/add-category.html'
    context = {
        'form': form
    }
    return render(request, template, context)


def blog_categories(request):
    categories = PostCategory.objects.all()
    template = 'dashboard/blog/category/categories.html'
    context = {
        'categories': categories,
    }
    return render(request, template, context)


def add_post(request):
    template = 'dashboard/blog/post/add-post.html'
    context = {}
    return render(request, template, context)


def posts_list(request):
    posts = Post.objects.all()
    template = 'dashboard/blog/post/posts-list.html'
    context = {
        'posts': posts,
    }
    return render(request, template, context)
