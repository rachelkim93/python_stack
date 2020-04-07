from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^dashboard$', views.dashboard),
    url(r'^logout$', views.logout),
    url(r'^view/(?P<user_id>\d+)$', views.view),
    url(r'^new/(?P<user_id>\d+)$', views.new),
    url(r'^new_job$', views.new_job),
    url(r'^edit/(?P<job_id>\d+)$', views.edit),
    url(r'^edit_job/(?P<job_id>\d+)$', views.edit_job),
    url(r'^delete/(?P<job_id>\d+)$', views.delete),
    url(r'^addJob$', views.addJob),
    url(r'^giveUp$', views.giveUp),
    url(r'^finish_job', views.finishJob),
]