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
from account.models import Apps


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    deviceName = models.CharField(max_length=100, blank=True, default='')
    advertising_id = models.CharField(max_length=100, blank=True, default='')
    idfa = models.CharField(max_length=100, blank=True, default='')
    appsflyer_int = models.BooleanField(default=False)
    bundle_id = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.PROTECT)
    # highlighted = models.TextField()

    class Meta:
        ordering = ('created',)

class InboundEmail(models.Model):
    inboundEmail = models.EmailField(max_length=70,blank=True, null= True)
    properEmail = models.BooleanField(default=True)
    emailSentToUS = models.BooleanField(default=False)
    # created = models.DateTimeField(auto_now_add=True)
    # class Meta:
        # ordering = ('created',)
# Send emails: https://simpleisbetterthancomplex.com/tutorial/2017/05/27/how-to-configure-mailgun-to-send-emails-in-a-django-app.html

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    companyName = models.CharField(max_length=100, blank=True,default='')
    companyWebsite = models.CharField(max_length=100, blank=True,default='')
    email = models.CharField(max_length=100, blank=True)    
    email_confirmed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    # birth_date = models.DateField(null=True, blank=True)
    class Meta:
        ordering = ('created',)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
        print(token.key)
        Profile.objects.create(user=instance)
        # print("potato")

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



# GENDER_CHOICES = (
# ('M', 'Male'),
# ('F', 'Female'),
# ('P', 'Prefer not to answer'),
# )

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, related_name='profile')
#     nickname = models.TextField(max_length=64, null=True, blank=True)
#     dob = models.DateField(null=True, blank=True)
#     gender = models.CharField(max_length=1, 
#                               choices=GENDER_CHOICES, default='M')
#     bio = models.TextField(max_length=1024, null=True, blank=True)
    


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, **kwargs):
    if kwargs.get('created', False):
        # UserProfile.objects.get_or_create(user=kwargs.get('instance'))
        print("it's working meow")

@receiver(post_save, sender=Snippet)
def ensure_snippet_exists(sender,instance, **kwargs):
    if kwargs.get('created', False):
        # UserProfile.objects.get_or_create(user=kwargs.get('instance'))
        d = datetime.now(timezone.utc).astimezone()
        currentTime = d.isoformat()
        print(d)
        print("it's working meow!!!")
        print(instance.deviceName)
        print(instance.advertising_id)
        print(instance.idfa)
        print(instance.appsflyer_int)
        print(instance.bundle_id)
        print(instance.owner)
        print(instance.id)
        print(uuid.uuid4())
        appsflyer_api_keyDict = Apps.objects.filter(owner=instance.owner).values('appsflyer_api_key')        
        for value in appsflyer_api_keyDict:
            print(value)
            print(list(value.values())[0])
            if value == "q":
                payload = {'subject_request_id': uuid.uuid4(), 'subject_request_type': 'erasure', 'submitted_time':currentTime,
                 "subject_identities": [
                      { 
                        "identity_type": "ios_advertising_id",
                        "identity_value": instance.idfa,
                        "identity_format": "raw"
                      } ],
                        "api_version": "0.1",
                        "property_id": instance.bundle_id,
                        "status_callback_urls": [
                        "https://examplecontroller.com/opengdpr_callbacks"
                         ]  }
                response = requests.post('https://hq1.appsflyer.com/gdpr/stub?api_token=3bdacf41-c341-4d60-9929-31c143b39bb2',  data = payload)
                print(response.status_code)
                print("RESPONSE TEXT:")
                print(response.text)
                # print(response.status_code)





