from django.contrib import admin
from .models import PostCategory


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'create', 'update')
    ordering = ['name']


admin.site.register(PostCategory, PostCategoryAdmin)
