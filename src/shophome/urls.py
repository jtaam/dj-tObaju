from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^contact/$', views.contact, name='contact'),
]
