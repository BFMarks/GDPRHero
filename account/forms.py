#log/forms.py
from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from snippets.models import Snippet, Profile,InboundEmail
from account.models import Apps



class InputAPIKeysForm(forms.ModelForm):
    appsflyer_api_key = forms.CharField(max_length=100)
    amplitude_api_key = forms.CharField(max_length=100)

    class Meta:
        model = Apps
        exclude = ('owner','created',)