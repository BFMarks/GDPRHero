from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from snippets.models import Profile
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from account.forms import InputAPIKeysForm
from .models import Apps
from datetime import datetime, timezone
# Create your views here.

def account_home(request):
    if request.method == 'GET' and request.user.is_authenticated:
        userIsActive = request.user
        # print(request.user)
        profile = Profile.objects.filter(user=request.user)
        # print(profile)
        # print(list(profile.values()))
        token = Token.objects.filter(user=request.user)
        actualTokenString = list(token)[0]
        print(actualTokenString)
        # return render( request,'container.html')
    # return render(request, 'container.html', {
            # 'actualTokenString': actualTokenString,
            # 'form': form
        # })
    # else:
        #Error Handle
    if request.method == 'POST' and request.user.is_authenticated:
        appsData = Apps.objects.filter(owner=request.user)
        print(appsData)

        token = Token.objects.filter(user=request.user)
        actualTokenString = list(token)[0]
        print(request.user)
        d = datetime.now(timezone.utc).astimezone()
        currentTime = d.isoformat()
        form = InputAPIKeysForm(request.POST)
        if form.is_valid():
            print('form is valid')
            stmt = form.save()
            pass  # does nothing, just trigger the validation
        else:
            print('form is NOTvalid')
            form = InputAPIKeysForm()
        # keysInput_form = InputAPIKeysForm(data=request.POST)
        # if keysInput_form.is_valid():
        #     appsflyer_api_key = keysInput_form.cleaned_data['appsflyer_api_key']
        #     print("appsflyer_api_key@@@@@@@@@@@!")
        #     print(appsflyer_api_key)
    return render(request, 'container.html', {
            'actualTokenString': actualTokenString,
            'form': form
        })
