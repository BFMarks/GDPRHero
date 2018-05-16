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

# Create your models here.
class Apps(models.Model):
    # created = models.DateTimeField(auto_now_add=True)
    # appName = models.TextField(max_length=100, blank=True)
    appsflyer_api_key = models.TextField(max_length=100, blank=True)
    amplitude_api_key = models.CharField(max_length=100, blank=True) 
    owner = models.ForeignKey('auth.User', related_name='apps', on_delete=models.PROTECT)

    # highlighted = models.TextField()
    # class Meta:
        # ordering = ('created',)

        