from django.contrib import admin
from .models import Brand, CategoryGroup, Colours


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'create', 'update')


admin.site.register(Brand, BrandAdmin)


class CategoryGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(CategoryGroup, CategoryGroupAdmin)


class ColoursAdmin(admin.ModelAdmin):
    list_display = ['name', 'color_code']


admin.site.register(Colours, ColoursAdmin)
