from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add_blog_category/$', views.add_blog_category, name='add_blog_category'),
    url(r'^category/(?P<cid>[0-9]+)/edit/$', views.edit_blog_category, name='edit_blog_category'),
    url(r'^category/(?P<cid>[0-9]+)/delete/$', views.delete_blog_category, name='delete_blog_category'),
    url(r'^blog_categories/$', views.blog_categories, name='blog_categories'),
    url(r'^add_post/$', views.add_post, name='add_post'),
    url(r'^blog/(?P<pid>[0-9]+)/edit/$', views.edit_blog_post, name='edit_blog_post'),
    url(r'^blog/(?P<pid>[0-9]+)/delete/$', views.delete_blog_post, name='delete_blog_post'),
    url(r'^posts_list/$', views.posts_list, name='posts_list'),
    url(r'', views.dashboard, name='dashboard'),
]
