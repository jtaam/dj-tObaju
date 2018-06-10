from django.contrib import admin
from .models import Advantages, TopSlider, GetInspired, TopOffer


class TopOfferAdmin(admin.ModelAdmin):
    list_display = ('percentage', 'limit', 'create', 'update')


admin.site.register(TopOffer, TopOfferAdmin)


class TopSliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'create', 'update')


admin.site.register(TopSlider, TopSliderAdmin)


class AdvantagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'icon', 'status', 'create', 'update')


admin.site.register(Advantages, AdvantagesAdmin)


class GetInspiredAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'create', 'update')


admin.site.register(GetInspired, GetInspiredAdmin)
