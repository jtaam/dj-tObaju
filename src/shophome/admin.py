from django.contrib import admin
from .models import Advantages, TopSlider, GetInspired, TopOffer, Logo, Faq, ContactUsPage, AboutUs, StayInTouch


class LogoAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Logo, LogoAdmin)


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


class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'status', 'create')


admin.site.register(Faq, FaqAdmin)


class ContactUsPageAdmin(admin.ModelAdmin):
    list_display = ['corporate_name', 'street', 'city', 'call_center_phone']


admin.site.register(ContactUsPage, ContactUsPageAdmin)


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['title', 'create', 'update']


admin.site.register(AboutUs, AboutUsAdmin)


class StayInTouchAdmin(admin.ModelAdmin):
    list_display = ['facebook', 'twitter', 'emailus']


admin.site.register(StayInTouch, StayInTouchAdmin)
