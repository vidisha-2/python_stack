from django.conf.urls import url
from . import views         
urlpatterns = [
    url(r'^restful_users$', views.index),
    url(r'^restful_users/create$', views.create),
    url(r'^restful_users/new$', views.new),
    url(r'^restful_users/edit/(?P<id>\d+)$', views.edit, name='edit_this'),
    url(r'^restful_users/update/(?P<id>\d+)$', views.update, name='update_this'),
    url(r'^restful_users/delete/(?P<id>\d+)$', views.destroy, name='delete_this'),
    url(r'^restful_users/show/(?P<id>\d+)$', views.show, name='display_this')
]   