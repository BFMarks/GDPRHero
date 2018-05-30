#log/forms.py
from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from snippets.models import Snippet, Profile,InboundEmail
from account.models import Apps
from django import forms
from django.utils.crypto import get_random_string
from django import forms
from django.utils.crypto import get_random_string




class InputAPIKeysForm(forms.ModelForm):
    appsflyer_api_key = forms.CharField(max_length=100)
    amplitude_api_key = forms.CharField(max_length=100)

    class Meta:
        model = Apps
        exclude = ('owner','created',)

class AppForm(forms.ModelForm):
    store_url = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'https://itunes.apple.com/us/app/appName/id123456789?mt=8'}),label="Store URL:")
    ios_app = forms.TypedChoiceField(coerce=lambda x: x =='True', 
                                   choices=((True, 'iOS'), (False, 'Android') ),label="App Type:")
    

    # def __init__(self):
        
            # self.fields['ios_app'].initial  = True

    class Meta:
        model = Apps
        fields = ('ios_app','store_url')
        # widgets = {
        #     'yes_or_no': forms.RadioSelect
        # }
        # # exclude = ('appsflyer_api_key','amplitude_api_key',)


class AppEditForm(forms.ModelForm):
    # app_id = forms.CharField( widget=forms.TextInput(attrs={'placeholder': 'https://...'}))
    # ios_app = forms.TypedChoiceField(coerce=lambda x: x =='True', 
                                   # choices=((True, 'iOS'), (False, 'Android') ))

    appsflyer_api_key = forms.CharField(max_length=100,required=False)
    amplitude_api_key = forms.CharField(max_length=100,required=False)
    braze_api_key = forms.CharField(max_length=100,required=False)
    mixpanel_api_key = forms.CharField(max_length=100,required=False)
    urbanairship_api_key = forms.CharField(max_length=100,required=False)
    adjust_api_key = forms.CharField(max_length=100,required=False)
    branch_api_key = forms.CharField(max_length=100,required=False)

    appsflyer_bool = forms.BooleanField(required=False,initial=False,label='Enable AppsFlyer GDPR Compliance')
    amplitude_bool = forms.BooleanField(required=False,initial=False,label='Enable Amplitude GDPR Compliance')
    braze_bool = forms.BooleanField(required=False,initial=False,label='Enable Braze GDPR Compliance')
    mixpanel_bool = forms.BooleanField(required=False,initial=False,label='Enable AppsFlyer Mixpanel Compliance')
    urbanairship_bool = forms.BooleanField(required=False,initial=False,label='Enable Urban Airship GDPR Compliance')
    adjust_bool = forms.BooleanField(required=False,initial=False,label='Enable Adjust GDPR Compliance')
    branch_bool = forms.BooleanField(required=False,initial=False,label='Enable Branch GDPR Compliance')
    
    class Meta:
        model = Apps
        fields = ('appsflyer_api_key','amplitude_api_key','braze_api_key','mixpanel_api_key','urbanairship_api_key','adjust_api_key')


