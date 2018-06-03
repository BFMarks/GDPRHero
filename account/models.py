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
from django.utils import timezone

BOOL_CHOICES = ((True, 'Yes'), (False, 'No'))

# Create your models here.
class Apps(models.Model):
    #Unique 
    #All Keys
    created = models.DateTimeField(auto_now_add=True)
    app_id = models.TextField(max_length=100, blank=False)
    bundle_id = models.TextField(max_length=100, blank=True)
    ios_app = models.BooleanField(choices=BOOL_CHOICES)
    store_url = models.TextField(max_length=500, blank=True)
    image_url = models.TextField(max_length=500, blank=True)
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
    
    customer_user_bool = models.BooleanField(default=True)
    appsflyer_bool = models.BooleanField(default=True)
    amplitude_bool = models.BooleanField(default=True)
    braze_bool = models.BooleanField(default=True)
    mixpanel_bool = models.BooleanField(default=True)
    urbanairship_bool = models.BooleanField(default=True)
    branch_bool = models.BooleanField(default=True)
    adjust_bool = models.BooleanField(default=True)
    mixpanel_bool = models.BooleanField(default=True)
    urban_airship_bool = models.BooleanField(default=True)
    optimizely_bool = models.BooleanField(default=True)
    googleAnalytics_bool = models.BooleanField(default=True)
    facebook_bool = models.BooleanField(default=True)
    fabric_bool = models.BooleanField(default=True)
    amplitude_bool = models.BooleanField(default=True)
    branch_bool = models.BooleanField(default=True)
    braze_bool = models.BooleanField(default=True)
    adjust_bool = models.BooleanField(default=True)
    leanplum_bool = models.BooleanField(default=True)
    iterable_bool = models.BooleanField(default=True)
    subparam1_bool = models.BooleanField(default=True)
    subparam2_bool = models.BooleanField(default=True)
    subparam3_bool = models.BooleanField(default=True)

    # highlighted = models.TextField()
    # class Meta:
        # ordering = ('created',)

    # def __unicode__(self):
    #     return '%s' % self.app_id

    # @permalink
    # def get_absolute_url(self):
    #     return ('view_app', None, { 'slug': self.slug })

class DataProcessors(models.Model):
    created = models.DateTimeField(default=timezone.now)
    gdpr_email = models.TextField(max_length=100, blank=False)
    contact = models.TextField(max_length=100, blank=False)
    processor_id = models.TextField(max_length=100, blank=False, default='customer_user_id')
    sendEmails = models.BooleanField(default=False)
    processor_bool_name = models.TextField(max_length=100, blank=False, default='customer_user_bool')

class AppsFlyerResponse(models.Model):
    created = models.DateTimeField(default=timezone.now)
    subject_request_id = models.CharField(max_length=100, blank=True) 
    received_time = models.DateTimeField(blank=True) 
    expected_completion_time = models.DateTimeField(blank=True) 
    encoded_request = models.CharField(max_length=1000, blank=True) 

# EXAMPLE:
# {
#     "subject_request_id": "20b9c186-2288-4599-b32b-62184e1c1e47",
#     "received_time": "2018-06-03T03:50:06.112Z",
#     "expected_completion_time": "2018-07-03T23:59:59.999Z",
#     "encoded_request": "eyJzdWJqZWN0X3JlcXVlc3RfaWQiOiIyMGI5YzE4Ni0yMjg4LTQ1OTktYjMyYi02MjE4NGUxYzFlNDciLCJzdWJqZWN0X3JlcXVlc3RfdHlwZSI6ImVyYXN1cmUiLCJzdWJtaXR0ZWRfdGltZSI6IjIwMTgtMDUtMjVUMTU6MDA6MDBaIiwic3ViamVjdF9pZGVudGl0aWVzIjpbeyJpZGVudGl0eV90eXBlIjoiaW9zX2FkdmVydGlzaW5nX2lkIiwiaWRlbnRpdHlfdmFsdWUiOiJFQTNFMTY4Mi01RUVCLTQzNkMtOUVDQi05QTgxQzc4ODFBQUEiLCJpZGVudGl0eV9mb3JtYXQiOiJyYXcifV0sImFwaV92ZXJzaW9uIjoiMC4xIiwicHJvcGVydHlfaWQiOiJpZDkzMTYzOTI1NCIsInN0YXR1c19jYWxsYmFja191cmxzIjpbXX0="
# }