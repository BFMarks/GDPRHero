from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth.models import User
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
import requests
import json
from datetime import datetime
import uuid
from django.db.models import F
from rest_framework.authtoken.models import Token
from account.models import Apps
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.template.defaultfilters import slugify

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
    optimizely_user_id = models.CharField(max_length=100, blank=True, default='')
    googleAnalytics_user_id = models.CharField(max_length=100, blank=True, default='')
    facebook_user_id = models.CharField(max_length=100, blank=True, default='')
    clever_tap_user_id = models.CharField(max_length=100, blank=True, default='')
    fabric_user_id = models.CharField(max_length=100, blank=True, default='')
    leanplum_user_id = models.CharField(max_length=100, blank=True, default='')
    iterable_user_id = models.CharField(max_length=100, blank=True, default='')
    subparam1_user_id = models.CharField(max_length=100, blank=True, default='')
    subparam2_user_id = models.CharField(max_length=100, blank=True, default='')
    subparam3_user_id = models.CharField(max_length=100, blank=True, default='')
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
        
        GDPR is a pain for business but let's make it as easy as possible to get compliant!  Our team will reach out to you shortly.
        
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

@receiver(pre_save, sender=Snippet)
def ensure_snippet_can_be_saved(sender, instance, *args, **kwargs):
    appIdObject = Apps.objects.filter(app_id=instance.app_id).values('app_id')
    appOwnerObject = Apps.objects.filter(owner=instance.owner).values('app_id')        
    print(appIdObject)
    print(appOwnerObject)
    # App and Owner are The Same
    if appIdObject[0] not in appOwnerObject:
        raise Exception('Not-The-Right-App-ID-Hero')
        print("maybe not a match?")

@receiver(post_save, sender=User)
def ensure_profile_exists(sender, **kwargs):
    if kwargs.get('created', False):
        # UserProfile.objects.get_or_create(user=kwargs.get('instance'))
        print("it's working meow")

@receiver(post_save, sender=Snippet)
def ensure_snippet_exists(sender,instance, **kwargs):
    if kwargs.get('created', False):
        print(instance)
        print("it's working meow!!!")
        print(instance.app_id)
        instance_UUID_hero = str(uuid.uuid4())  
        appIdObject = Apps.objects.filter(app_id=instance.app_id).values('app_id')
        appOwnerObject = Apps.objects.filter(owner=instance.owner).values('app_id')    
        local_time = datetime.now(timezone.utc).astimezone()
        created = local_time.isoformat()    
        app_name = str(instance.owner)

        # App and Owner are The Same
        appsflyer_api_keyDict = list(Apps.objects.filter(app_id=instance.app_id).values('appsflyer_api_key'))[0]
        appsFlyerAPI_token = appsflyer_api_keyDict.get("appsflyer_api_key")
        if appsFlyerAPI_token != "":
            appsFlyerCompliance(instance_UUID_hero, instance.idfa, instance.app_id, appsFlyerAPI_token, app_name, created)

        adjust_api_keyDict = list(Apps.objects.filter(app_id=instance.app_id).values('adjust_api_key'))[0]
        adjustAPI_token = adjust_api_keyDict.get("adjust_api_key")
        if adjustAPI_token != "":
            adjustCompliance(adjustAPI_token, instance.idfa)

        amplitude_api_keyDict = list(Apps.objects.filter(app_id=instance.app_id).values('amplitude_api_key'))[0]
        amplitudeAPI_token = amplitude_api_keyDict.get("amplitude_api_key")
        if amplitudeAPI_token != "":
            amplitudeCompliance(amplitudeAPI_token, instance.customer_user_id, instance.amplitude_user_id)

        braze_api_keyDict = list(Apps.objects.filter(app_id=instance.app_id).values('braze_api_key'))[0]
        brazeAPI_token = braze_api_keyDict.get("braze_api_key")
        if brazeAPI_token != "":
            brazeCompliance(brazeAPI_token, instance.customer_user_id, instance.braze_user_id)

        customer_endpointDict = list(Apps.objects.filter(app_id=instance.app_id).values('customer_endpoint'))[0]
        customer_endpoint_url = customer_endpointDict.get("customer_endpoint")
        if customer_endpoint_url != "":
            customerEndpointCompliance(instance.created,instance.deviceName,instance.advertising_id,instance.idfa,instance.bundle_id,instance.amplitude_user_id,
                instance.braze_user_id,instance.mixpanel_user_id,instance.urbanairship_user_id,instance.branch_user_id,instance.adjust_user_id,
                instance.customer_user_id,instance.app_id,instance.optimizely_user_id,instance.googleAnalytics_user_id,instance.facebook_user_id,instance.clever_tap_user_id,
                instance.fabric_user_id,instance.subparam1_user_id,instance.subparam2_user_id,instance.subparam3_user_id,instance.owner)

def customerEndpointCompliance(created, deviceName, advertising_id, idfa, bundle_id, amplitude_user_id, braze_user_id, mixpanel_user_id, urbanairship_user_id, 
    branch_user_id, adjust_user_id, customer_user_id, app_id, optimizely_user_id, googleAnalytics_user_id, facebook_user_id, 
    clever_tap_user_id, fabric_user_id, subparam1_user_id, subparam2_user_id, subparam3_user_id, owner ):
    endpoint_url = customer_endpoint_url
    headers = {"Content-Type":"application/json"}
    payload = {
            "created" : instance.created,
            "deviceName" : instance.deviceName,
            "advertising_id" : instance.advertising_id,
            "idfa" : instance.idfa,
            "bundle_id" : instance.bundle_id,
            "amplitude_user_id" : instance.amplitude_user_id,
            "braze_user_id" : instance.braze_user_id,
            "mixpanel_user_id" : instance.mixpanel_user_id,
            "urbanairship_user_id" : instance.urbanairship_user_id,
            "branch_user_id" : instance.branch_user_id,
            "adjust_user_id" : instance.adjust_user_id,
            "customer_user_id" : instance.customer_user_id,
            "app_id" : instance.app_id,
            "optimizely_user_id" : instance.optimizely_user_id,
            "googleAnalytics_user_id" : instance.googleAnalytics_user_id,
            "facebook_user_id" : instance.facebook_user_id,
            "clever_tap_user_id" : instance.clever_tap_user_id,
            "fabric_user_id" : instance.fabric_user_id,
            "subparam1_user_id" : instance.subparam1_user_id,
            "subparam2_user_id" : instance.subparam2_user_id,
            "subparam3_user_id" : instance.subparam3_user_id,
            "owner" : instance.owner
    }            
    response = requests.post(endpoint_url, data=json.dumps(payload), headers=headers)
    print(response)
    print(response.text)
    print(payload)

def brazeCompliance(brazeAPI_token, customer_user_id ,braze_user_id ):
    print("amplitude Integrated")
    endpoint_url = 'https://rest.iad-01.braze.com/users/delete'
    headers = {"Content-Type":"application/json"}
    payload = {
    "api_key": brazeAPI_token,
    "external_ids": [customer_user_id],
    "braze_ids": [braze_user_id]
    }
    response = requests.post(endpoint_url, data=json.dumps(payload), headers=headers)
    print(response)
    print(response.text)
    print(payload)


def amplitudeCompliance(amplitudeAPI_token, customer_user_id, amplitude_user_id):
    print("amplitude Integrated")
    endpoint_url = 'https://amplitude.com/api/2/deletions/users'
    headers = {"API_KEY":amplitudeAPI_token}
    payload = {
    "amplitude_ids": [amplitude_user_id],
    "user_ids": [customer_user_id],
    "requester": app_name + " (GDPRHero.io)"
    }
    response = requests.post(endpoint_url,  data = payload, headers=headers)
    print(response)
    print(response.text)
    print(payload)

def appsFlyerCompliance(instance_UUID_hero, idfa_from_instance, app_id_from_instance, AppsFlyerAPI_token, app_name, created):
    print("AppsFlyer Integrated")
    endpoint_url = 'https://hq1.appsflyer.com/gdpr/opengdpr_requests?api_token='+ AppsFlyerAPI_token+'1'
    headers = {'Host':app_name+'.com',  'Accept': 'application/json', 'Content-type': 'application/json' }
    payload = {'subject_request_id': instance_UUID_hero, 'subject_request_type': 'erasure', 'submitted_time':created,
     "subject_identities": [
          { 
            "identity_type": "ios_advertising_id",
            "identity_value": idfa_from_instance,
            "identity_format": "raw"
          } ],
            "api_version": "0.1",
            "property_id": 'id'+ app_id_from_instance,
            "status_callback_urls": [
            #record response
            "https://examplecontroller.com/opengdpr_callbacks"
             ]  }
    response = requests.post(endpoint_url,  data=json.dumps(payload), headers=headers)
    if response != 201:
        print(response)
        print("FAILED RESPONSE")
    print("RESPONSE TEXT:")
    print(response.text)
    print(payload)

def adjustCompliance(adjustAPI_token, idfa):
    print("Adjust Integrated")
    endpoint_url = "https://gdpr.adjust.com/gdpr_forget_device?s2s=1&app_token=" + adjustAPI_token + "&idfa=" + idfa
    response = requests.get(endpoint_url)
    print(response)
    print("RESPONSE TEXT:")
    print(response.text)
    print(payload)



#  GDPR ENDPOINT:
# http://help.adjust.com/en/manage-your-data/data-privacy/gdpr#gdpr-api-requirements 
# "https://gdpr.adjust.com/gdpr_forget_device?s2s=1&app_token=kwrqhymtnsr2&idfa=9C5CBC1D-4F42-4764-A5E6-84DAF3D24707"

# https://amplitude.zendesk.com/hc/en-us/articles/360000398191-User-Privacy-API
# > curl -s -u API_KEY:SECRET_KEY --data amplitude_ids=1234567890  --data requester='somebody@acmecorp.com' 'https://amplitude.com/api/2/deletions/users' | json_pp
# {
#    "day" : "2018-02-04",
#    "amplitude_ids" : [
#       {
#          "requested_on_day" : "2018-01-26",
#          "amplitude_id" : 1234567890,
#          "requester" : "somebody@acmecorp.com"
#       }
#    ],
#    "status" : "staging"
# }

# https://www.braze.com/documentation/REST_API/#user-delete-endpoint
# https://rest.iad-01.braze.com/users/delete
# POST https://YOUR_REST_API_URL/users/delete
# Content-Type: application/json
# {
#   "api_key" : (required, string) App Group REST API Key,
#   "external_ids" : (optional, array of string) external ids for the users to delete,
#   "braze_ids" : (optional, array of string) Braze User Identifiers for the users to delete
# }

# https://help.optimizely.com/Account_Settings/Request_or_delete_records_for_EU_General_Data_Protection_Regulation_(GDPR)


# https://developers.google.com/analytics/devguides/config/userdeletion/v3/reference/userDeletion/userDeletionRequest
# https://developers.google.com/analytics/devguides/config/userdeletion/v3/reference/userDeletion/userDeletionRequest/upsert