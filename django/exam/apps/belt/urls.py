from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
    url(r'^delete/(?P<wish_id>\d+)$', views.delete),
    url(r'^new/(?P<user_id>\d+)$', views.new),
    url(r'^new_wish$', views.new_wish),
    url(r'^grant/(?P<wish_id>\d+)$', views.grant),
    url(r'^edit/(?P<wish_id>\d+)$', views.edit),
    url(r'^edit_wish/(?P<wish_id>\d+)$', views.edit_wish),
    url(r'^like/(?P<wish_id>\d+)$', views.like),
    url(r'^stats$', views.stats),
]