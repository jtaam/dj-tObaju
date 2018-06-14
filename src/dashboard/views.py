from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import PostCategory, Post
from .forms import PostCategoryForm, PostForm


###############################
# Dashboard index
###############################
def dashboard(request):
    current_user = request.user
    template = 'dashboard/index.html'
    context = {
        'current_user': current_user,
    }
    return render(request, template, context)


###############################
# Blog Category
###############################
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


def edit_blog_category(request, cid):
    unique_category = get_object_or_404(PostCategory, id=cid)
    form = PostCategoryForm(request.POST or None, request.FILES or None, instance=unique_category)
    if form.is_valid():
        form.save()
        messages.info(request, 'Successfully updated the category.')
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


def delete_blog_category(request, cid):
    unique_category = get_object_or_404(PostCategory, pk=cid)
    unique_category.delete()
    messages.info(request, 'Successfully deleted the blog category.')
    return redirect('/dashboard/blog_categories/')


###############################
# Blog Post
###############################
def add_post(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        messages.info(request, 'Successfully created a new blog post.')
        return redirect('/dashboard/posts_list/')
    template = 'dashboard/blog/post/add-post.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def posts_list(request):
    posts = Post.objects.all()
    template = 'dashboard/blog/post/posts-list.html'
    context = {
        'posts': posts,
    }
    return render(request, template, context)
