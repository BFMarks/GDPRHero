from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from snippets.models import Profile, Snippet
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from account.forms import InputAPIKeysForm, AppForm, AppEditForm
from .models import Apps
from datetime import datetime, timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
import urllib.request
import lxml.html
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime


# Create your views here.

@login_required
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

    return render(request, 'account.html', {
            'actualTokenString': actualTokenString,
            # 'form': form
        })

@login_required(login_url='/login/')
def app_new(request):
    form = AppForm()
    token = Token.objects.filter(user=request.user)
    actualTokenString = list(token)[0]
    print(actualTokenString)
    if request.method == "POST":
        dataToGiveForm={'owner': request.user}
        form = AppForm(request.POST, dataToGiveForm)
        if form.is_valid():
            print("VALID")
            app = form.save(commit=False)
            app.owner = request.user
            app.store_url = form.cleaned_data['store_url']
            app.ios_app = form.cleaned_data['ios_app']
            print(app.store_url)
            
            returnFromStore = takeURL(app.store_url)
            app.image_url = returnFromStore[0]
            app.app_name = returnFromStore[1]
            app.app_id = returnFromStore[2]
            print(returnFromStore)
            app.save()
            return redirect('app_edit', pk=app.pk)
    else:
        form = AppForm()
    return render(request, 'app_new.html', {'form': form,
        'actualTokenString': actualTokenString,
        })

@login_required(login_url='/login/')
def app_detail(request, pk): 
    app = get_object_or_404(Apps, pk=pk)
    token = Token.objects.filter(user=request.user)
    actualTokenString = list(token)[0]
    return render(request, 'account.html', {'app': app,
        'actualTokenString': actualTokenString,
        })

def app_list(request): 
    apps = Apps.objects.filter(owner=request.user)
    print(apps)
    if request.method == "GET" and request.user.is_authenticated:
        return render(request, 'app_home.html', {'apps': apps,})
    

def app_edit(request, pk):
    app = get_object_or_404(Apps, pk=pk)
    token = Token.objects.filter(user=request.user)
    actualTokenString = list(token)[0]
    if request.method == "POST":
        dataToGiveForm={'owner': request.user }
        form = AppEditForm(request.POST, dataToGiveForm,instance=app)
        if form.is_valid():
            print("is_valid")
            # app = form.save(commit=False)
            app.owner = request.user
            app.appsflyer_api_key = form.cleaned_data['appsflyer_api_key']
            app.amplitude_api_key = form.cleaned_data['amplitude_api_key']
            print(app.appsflyer_api_key)
            app.save()
            return redirect('app_detail', pk=app.pk)
    else:
        form = AppEditForm(instance=app)
    return render(request, 'app_edit.html', {'form': form, 'actualTokenString':actualTokenString, 'app': app})

@login_required(login_url='/login/')
def configure(request, pk): 
    app = get_object_or_404(Apps, pk=pk)
    token = Token.objects.filter(user=request.user)
    actualTokenString = list(token)[0]
    return render(request, 'configure.html', {'app': app,
        'actualTokenString': actualTokenString,
        })    

def getCSV(request):
    if request.method == "GET" and request.user.is_authenticated:
        df = pd.DataFrame(list(Snippet.objects.filter(owner=request.user)))
        print(df)
        df.to_csv("/Users/bryanmarks/GDPRHero/Data.csv")
        apps = Apps.objects.filter(owner=request.user)
        print(apps)
        return render(request, 'app_home.html', {'apps': apps,})

# def appsflyer_int(request):
#     if request.method == 'GET' and request.user.is_authenticated:
#         appsData = Apps.objects.all()
#         print("appsData")
#         print(appsData)

#         token = Token.objects.filter(user=request.user)
#         actualTokenString = list(token)[0]
#         # current_user = request.user
#         form = InputAPIKeysForm()
#         print(form)

#     if request.method == 'POST' and request.user.is_authenticated:
#         appsData = Apps.objects.filter(owner=request.user)
#         print(appsData)

#         token = Token.objects.filter(user=request.user)
#         actualTokenString = list(token)[0]
#         print(request.user)
#         d = datetime.now(timezone.utc).astimezone()
#         currentTime = d.isoformat()
#         dataToGiveForm={'owner_id': request.user ,'app_id':'testApp'}
#         print(dataToGiveForm)

#         form = InputAPIKeysForm(request.POST,dataToGiveForm)
#         if form.is_valid():
#             print('form is valid')
#             print(form)
#             obj = Apps()
#             obj.app_id = form.cleaned_data['app_id']
#             obj.appsflyer_api_key = form.cleaned_data['appsflyer_api_key']
#             # obj.owner = form.cleaned_data['owner']
#             appsflyer_int_working = Apps.objects.create(owner=request.user)
#             print(appsflyer_int)
#             obj.save()
#             return render(request, 'container.html')
#             # 'actualTokenString': actualTokenString,
#             # 'form': form
#         # })
#         else:
#             print('form is NOTvalid')
#             form = InputAPIKeysForm()
#         # keysInput_form = InputAPIKeysForm(data=request.POST)
#         # if keysInput_form.is_valid():
#         #     appsflyer_api_key = keysInput_form.cleaned_data['appsflyer_api_key']
#         #     print("appsflyer_api_key@@@@@@@@@@@!")
#         #     print(appsflyer_api_key)
#     return render(request, 'container.html', {
#             'actualTokenString': actualTokenString,
#             'form': form
#         })


def takeURL(url):
    # url = "https://itunes.apple.com/us/app/pinterest/id429047995?mt=8"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # images = soup.find_all('srcset')
    images = soup.findAll('img')
    for image in images:
        appImage = image['src']
        print(appImage)
        break

    # div = soup.find('h1', {"class" : "product-header__title product-header__title--app-header"})
    appTitle = soup.select('h1.product-header__title')[0].text.strip()
    
    titleTextPreSplit = re.sub(r'\d+', '', appTitle)
    titleText = titleTextPreSplit.split("\n")[0]
    print(titleText)
    
    spliceURL = url.split("id")[1]
    app_id_from_store = spliceURL.split("?")[0]

    return [appImage, titleText, app_id_from_store]
    # return  render(request, 'app_home.html',{
    #     'appImage':appImage,
    #     'titleText':titleText,
    #     'app_id_from_store':app_id_from_store
    #     })
        

        # for items in thelist:
            # print(list(items))
    #print alternate text
        # wholeThingAsString = string(image)
        # print(wholeThingAsString.split("world",1)[1])
    
    
    # print(doc)
