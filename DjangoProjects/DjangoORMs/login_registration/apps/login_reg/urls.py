from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index),
    url(r'^the_wall/mainpage/(?P<id>\d+)$', views.wall),
    url(r'^register$', views.register),
    url(r'^success/(?P<id>\d+)$', views.success),
    url(r'^login$', views.login),
]