from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from log.forms import LoginForm
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    url(r'^account/$', views.account_home,name='account'),    
    # url(r'^appsflyer-integration/$', views.appsflyer_int,name='appsflyer_int'),  
    url(r'^app/new/$', views.app_new, name='app_new'),  
    url(r'^applist/$', views.app_list, name='app_list'),  
    url(r'^app/(?P<pk>[0-9]+)/$', views.app_detail, name='app_detail'),
    url(r'^app/(?P<pk>\d+)/edit/$', views.app_edit, name='app_edit'),
    url(r'^app/(?P<pk>\d+)/configure/$', views.configure, name='configure'),

    url(r'^takeURL/$', views.takeURL, name='takeURL'),  
    url(r'^getCSV/$', views.getCSV, name='getCSV'),  




]
