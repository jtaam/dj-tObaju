from django import forms
from blog.models import PostCategory, Post


class PostCategoryForm(forms.ModelForm):
    class Meta:
        model = PostCategory
        fields = ['name', 'description', 'image', 'status']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'description', 'category', 'image', 'status']
