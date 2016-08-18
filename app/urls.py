# coding:utf-8
from django.conf.urls import url, patterns, include
import views.index

urlpatterns = [
    url('^graph/$', views.index.painting, name="index"),
    url('^graph/node/update_node_position/$', views.index.update_position, name="update_position"),
    url('^graph/node/update_root_position/$', views.index.update_root_position, name="update_root_position"),
]
