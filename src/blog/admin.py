from django.contrib import admin
from .models import PostCategory, Post


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'create', 'update')
    ordering = ['name']


admin.site.register(PostCategory, PostCategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'category', 'create', 'update')


admin.site.register(Post, PostAdmin)
