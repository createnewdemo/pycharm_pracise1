
from django.conf.urls import url
from app01 import views

urlpatterns = [
    url(r'^blog/$', views.blog,name='blog'),#  路径：/app01/blog -->> blog
    url(r'^index/$', views.index),#  路径：/app01/index
    url(r'^blogs/(\d{4})/\d{2}$', views.blogs,name='blogs'),
]
