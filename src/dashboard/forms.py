from django import forms
from blog.models import PostCategory


class PostCategoryForm(forms.ModelForm):
    class Meta:
        model = PostCategory
        fields = ['name', 'description', 'image', 'status']
