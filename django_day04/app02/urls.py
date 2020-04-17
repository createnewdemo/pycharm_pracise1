
from django.conf.urls import url
from app02 import views

urlpatterns = [
    url(r'^article/$', views.article),#  路径：/app01/blog
    url(r'^article/(?P<year>\d{4})/\d{2}$', views.articles),
]
