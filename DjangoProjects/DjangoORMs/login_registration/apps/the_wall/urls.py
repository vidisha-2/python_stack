from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^post_msg$', views.post_message),
    url(r'^post_comment$',views.post_comment),
    url(r'^delete_comment/(?P<id>\d+)$', views.delete_comment) # This line has changed! Notice that urlpatterns is a list, the comma is in
]       