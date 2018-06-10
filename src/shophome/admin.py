from django.contrib import admin
from .models import TopSlider


class TopSliderAdmin(admin.ModelAdmin):
    list_display = ('name','status','create','update')


admin.site.register(TopSlider, TopSliderAdmin)
