from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from log.forms import LoginForm
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^account/$', views.account_home,name='account'),    
  

]
