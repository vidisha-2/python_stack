from django.conf.urls import url
from . import views
urlpatterns = [ url(r'^random_word$', views.index),
				url(r'^random_word/increment$', views.generate),
				url(r'^random_word/reset/$', views.reset)	]