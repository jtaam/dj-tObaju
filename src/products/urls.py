from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<pid>[0-9]+)/$', views.product_detail, name='product_detail'),
    # url(r'^category/(?P<category>[-w]+)/$', views.products_list_by_category, name='products_list_by_category'),
    url(r'^', views.products_list, name='products_list'),
    # url(r'^brand/(?P<slug>[-\w]+)/$', view=views.brand_detail, name='brand_detail',),
]
