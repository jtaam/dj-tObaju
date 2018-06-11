from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.products_list, name='products_list'),
    # url(r'^brand/(?P<slug>[-\w]+)/$', view=views.brand_detail, name='brand_detail',),
]
