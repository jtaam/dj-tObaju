from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<pid>[0-9]+)/$', views.blog_detail, name='blog_detail'),
    url(r'', views.blog_list, name='blog_list'),
]
