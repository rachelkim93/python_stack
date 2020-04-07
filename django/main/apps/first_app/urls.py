from django.conf.urls import url
from . import views 
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new/$', views.new),
    url(r'^create/$', views.create),
    url(r'^(?P<number>\w+)$', views.show),
    url(r'^(?P<number>\w+)/edit$', views.edit),
    url(r'^(?P<number>\w+)/destroy$', views.destroy)
]    
