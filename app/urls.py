# coding:utf-8
from django.conf.urls import url, patterns, include
from django.views.generic import TemplateView
import views.index
import views.user

urlpatterns = [
    url('^Cam$', TemplateView.as_view(template_name="app/indexCam.html")),
    url('^graph/$', views.index.painting, name="index"),
    url('^graph/node/update_node_position/$', views.index.update_position, name="update_position"),
    url('^graph/node/update_root_position/$', views.index.update_root_position, name="update_root_position"),
    url('^user/login/$', views.user.login, name="user_login"),
    url('^user/arealist/$', views.user.getAreaList, name="getAreaList"),
    url('^user/linelist/$', views.user.getLineList, name="getLineList"),
]
