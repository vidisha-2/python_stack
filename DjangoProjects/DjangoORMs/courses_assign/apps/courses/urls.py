from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/create$', views.create),
    url(r'^destroy/(?P<id>\d+)$', views.show),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete_this'),   # This line has changed! Notice that urlpatterns is a list, the comma is in
]  