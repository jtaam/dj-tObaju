from django.contrib import admin
from .models import Brand


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'create', 'update')
    # exclude = ('slug',)


admin.site.register(Brand, BrandAdmin)
