from django.conf.urls import url
from apps.times import views 
urlpatterns = (
    url(r'^$', views.index, name='index'),
)
