from django.contrib import admin
from .models import Brand, CategoryGroup, Colours, ProductCategory, Product, ProductShareLinks


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'create', 'update')


admin.site.register(Brand, BrandAdmin)


class CategoryGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(CategoryGroup, CategoryGroupAdmin)


class ColoursAdmin(admin.ModelAdmin):
    list_display = ['name', 'color_code']


admin.site.register(Colours, ColoursAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'cat_group', 'status', 'create', 'update')


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'category', 'brand', 'sold', 'stock', 'price', 'new_price')


admin.site.register(Product, ProductAdmin)


class ProductShareLinksAdmin(admin.ModelAdmin):
    list_display = ('sitename', 'create', 'update')
    exclude = ('create', 'update')


admin.site.register(ProductShareLinks, ProductShareLinksAdmin)
