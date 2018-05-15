from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
# from django.contrib.auth import views
from log.forms import LoginForm
from . import views
from django.contrib.auth import views as auth_views
from log import views as core_views


urlpatterns = [

    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^', include('snippets.urls')),
    # url(r'^', include('log.urls')),

    url(r'^$', views.home,name='home'),
    url(r'home/^$', views.home,name='home'),
    # url(r'^home/$', views.home, {'template_name': 'home.html'},name = 'home_logged_in'),    
    url(r'^login/$', views.loginView,  name='login'),
    
    # Change next page for logout
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    # url(r'^accounts/', include('registration.backends.hmac.urls')),
   # How To: https://gearheart.io/blog/tutorial-django-user-registration-and-authentication/
    # url(r'^signup2/$', include('social_django.urls', namespace='social')),
   
   

]
