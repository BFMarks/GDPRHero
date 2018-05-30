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
from datetime import datetime
import uuid
from django.db.models import F
from rest_framework.authtoken.models import Token
from account.models import Apps
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives

class Snippet(models.Model):
    created = models.DateTimeField(default=timezone.now)
    deviceName = models.CharField(max_length=100, blank=True, default='')
    advertising_id = models.CharField(max_length=100, blank=True, default='')
    idfa = models.CharField(max_length=100, blank=True, default='')
    bundle_id = models.CharField(max_length=100, blank=True, default='')
    amplitude_user_id = models.CharField(max_length=100, blank=True, default='')
    braze_user_id = models.CharField(max_length=100, blank=True, default='') 
    mixpanel_user_id = models.CharField(max_length=100, blank=True, default='') 
    urbanairship_user_id = models.CharField(max_length=100, blank=True, default='')
    branch_user_id = models.CharField(max_length=100, blank=True, default='')
    adjust_user_id = models.CharField(max_length=100, blank=True, default='')
    customer_user_id = models.CharField(max_length=100, blank=True, default='')
    app_id = models.CharField(max_length=100, blank=False, default='')
    optimizely_id = models.CharField(max_length=100, blank=True, default='')
    googleAnalytics_id = models.CharField(max_length=100, blank=True, default='')
    facebook_user_id = models.CharField(max_length=100, blank=True, default='')
    clever_tap_id = models.CharField(max_length=100, blank=True, default='')
    fabric_id = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.PROTECT)
    # highlighted = models.TextField()
    class Meta:
        ordering = ('created',)

class InboundEmail(models.Model):
    inboundEmail = models.EmailField(max_length=70,blank=True, null= True)
    properEmail = models.BooleanField(default=True)
    emailSentToUS = models.BooleanField(default=False)
    created = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ('created',)

@receiver(post_save, sender=InboundEmail)
def send_post_inbound_email(sender,instance, **kwargs):
    if kwargs.get('created', False):
        text_content = """
        Hello!
        
        GDPR is a pain for bussiness but let's make it as easy as possible to get compliant!  Our team will reach out to you shortly.
        
        Kindest regards,
        
        GDPRHero Team"""
        print(instance.inboundEmail)
        email = EmailMultiAlternatives('Welcome To Pain Free GDPR Compliance!', text_content, 'Do Not Reply <do_not_replay@domain.com>', [instance.inboundEmail])
        email.send()
        emailToSales = EmailMultiAlternatives('We Have An Inbound Email!', instance.inboundEmail, 'Do Not Reply <do_not_replay@domain.com>', ['john@gdprhero.io'])
        emailToSales.send()
        return
        



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
        Profile.objects.create(user=instance)
        # print("potato")

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# @receiver(pre_save, sender=Snippet)
# def ensure_snippet_can_be_saved(sender, instance, *args, **kwargs):
#     instance.slug = slugify(instance.title)

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
        print(instance)
        print("it's working meow!!!")
        print(instance.app_id)
        print(instance.deviceName)
        print(instance.advertising_id)
        print(instance.idfa)
        
        print(instance.bundle_id)
        print(instance.owner)
        #PRINT APP ID
        print(instance.id)
        print(uuid.uuid4())
        appIdObject = Apps.objects.filter(app_id=instance.app_id).values('app_id')
        appOwnerObject = Apps.objects.filter(owner=instance.owner).values('app_id')        
        print(appIdObject)
        print(appOwnerObject)
        # App and Owner are The Same
        if appIdObject[0] in appOwnerObject:
            appObject = Apps.objects.filter(app_id=instance.app_id).values('appsflyer_api_key')
            appsflyer_api_keyDict  = list(appObject)[0]
            print("maybe not a match?")
            if appsflyer_api_keyDict.get("appsflyer_api_key") == "q":
                print("AppsFlyer Integrated")
                # change host
                headers = {'Host':'http://www.bryan.com',  'Accept': 'application/json', 'Content-type': 'application/json' }
                payload = {'subject_request_id': uuid.uuid4(), 'subject_request_type': 'erasure', 'submitted_time':"2018-05-19T15:00:00Z",
                 "subject_identities": [
                      { 
                        "identity_type": "ios_advertising_id",
                        "identity_value": instance.idfa,
                        "identity_format": "raw"
                      } ],
                        "api_version": "0.1",
                        "property_id": instance.bundle_id,
                        "status_callback_urls": [
                        #record response
                        "https://examplecontroller.com/opengdpr_callbacks"
                         ]  }
                response = requests.post('https://hq1.appsflyer.com/gdpr/stub?api_token=3bdacf41-c341-4d60-9929-31c143b39bb2',  data = payload, headers=headers)
                print(response)
                print("RESPONSE TEXT:")
                print(response.text)
                print(payload)





