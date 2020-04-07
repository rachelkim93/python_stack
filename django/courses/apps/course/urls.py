from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^addcourse$', views.addcourse),
    url(r'^removecourse/(?P<id>\d+)$', views.removecourse),
    url(r'^removethis/(?P<id>\d+)$', views.removethis),
]