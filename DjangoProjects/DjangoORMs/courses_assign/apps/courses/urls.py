from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/create$', views.create),
    url(r'^show$', views.show),
    url(r'^delete/(?P<id>\d+)$', views.destroy, name='delete_this'),   # This line has changed! Notice that urlpatterns is a list, the comma is in
]  