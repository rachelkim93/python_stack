from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^dashboard$', views.dashboard),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^add$', views.add),
    url(r'^show/(?P<user_id>\d+)$', views.show),
    url(r'^edit/(?P<user_id>\d+)$', views.edit),
    url(r'^edit_account/(?P<user_id>\d+)$', views.edit_account),
    url(r'^like/(?P<quote_id>\d+)$', views.like),
    url(r'^delete/(?P<quote_id>\d+)$', views.delete),
    url(r'^comment$', views.comment),
    url(r'^delete_comment/(?P<comment_id>\d+)$', views.delete_comment)
]