from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^terms-and-conditions/$', views.terms_and_conditions, name='terms_and_conditions'),
    url(r'^about-us/$', views.about_us, name='about_us'),
]
