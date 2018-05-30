from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import requests
from datetime import datetime, timezone   
import uuid
from django.db.models import F
from rest_framework.authtoken.models import Token
from django.db.models import permalink

BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

# Create your models here.
class Apps(models.Model):
    #Unique 
    #All Keys
    created = models.DateTimeField(auto_now_add=True)
    app_id = models.TextField(max_length=100, blank=False)
    bundle_id = models.TextField(max_length=100, blank=True)
    ios_app = models.BooleanField(choices=BOOL_CHOICES)
    store_url = models.TextField(max_length=100, blank=True)
    image_url = models.TextField(max_length=100, blank=True)
    app_name = models.TextField(max_length=100, blank=True)
    appsflyer_api_key = models.TextField(max_length=100, blank=True)
    amplitude_api_key = models.CharField(max_length=100, blank=True) 
    braze_api_key = models.CharField(max_length=100, blank=True) 
    mixpanel_api_key = models.CharField(max_length=100, blank=True) 
    urbanairship_api_key = models.CharField(max_length=100, blank=True) 
    branch_api_key = models.CharField(max_length=100, blank=True) 
    adjust_api_key = models.CharField(max_length=100, blank=True) 
    customer_endpoint = models.CharField(max_length=100, blank=True) 
    owner = models.ForeignKey('auth.User', related_name='apps', on_delete=models.PROTECT)
    
    appsflyer_bool = models.BooleanField(default=False)
    amplitude_bool = models.BooleanField(default=False)
    braze_bool = models.BooleanField(default=False)
    mixpanel_bool = models.BooleanField(default=False)
    urbanairship_bool = models.BooleanField(default=False)
    branch_bool = models.BooleanField(default=False)
    adjust_bool = models.BooleanField(default=False)
    customer_bool = models.BooleanField(default=False)

    # highlighted = models.TextField()
    # class Meta:
        # ordering = ('created',)

    # def __unicode__(self):
    #     return '%s' % self.app_id

    # @permalink
    # def get_absolute_url(self):
    #     return ('view_app', None, { 'slug': self.slug })

