from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^/$', views.index),
    url(r'^/new', views.new),
    url(r'^/show/(?P<uid>\d+)$', views.show),
    url(r'^/(?P<uid>\d+)/edit$', views.edit),
    url(r'^/create$', views.create),
    url(r'^/(?P<uid>\d+)/destroy$', views.destroy),
    url(r'^/update$', views.update),
    url(r'^/(?P<uid>\d+)$', views.show),
]