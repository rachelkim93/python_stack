from django.conf.urls import url, include
from . import views 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^quotes$', views.quotes),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^quote$', views.quote_post),
    url(r'^users/(?P<user_id>\d+)$', views.users),
    url(r'^account$', views.account),
    url(r'^update$', views.update),
    url(r'^dashboard$', views.dashboard),
    # url(r'^/(?P<uid>\d+)/edit$', views.edit),
]