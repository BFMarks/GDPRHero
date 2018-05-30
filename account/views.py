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
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.core import mail
import datetime
from django.utils import timezone

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
            app.braze_api_key = form.cleaned_data['braze_api_key']
            app.mixpanel_api_key = form.cleaned_data['mixpanel_api_key']
            app.urbanairship_api_key = form.cleaned_data['urbanairship_api_key']
            app.branch_api_key = form.cleaned_data['branch_api_key']
            app.adjust_api_key = form.cleaned_data['adjust_api_key']

            app.appsflyer_bool = form.cleaned_data['appsflyer_bool']
            app.amplitude_bool = form.cleaned_data['amplitude_bool']
            app.braze_bool = form.cleaned_data['braze_bool']
            app.mixpanel_bool = form.cleaned_data['mixpanel_bool']
            app.urbanairship_bool = form.cleaned_data['urbanairship_bool']
            app.branch_bool = form.cleaned_data['branch_bool']
            app.adjust_bool = form.cleaned_data['adjust_bool']
            
            print(app.appsflyer_api_key)
            print(app.appsflyer_bool)
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
    

def sendEmail(request):
    if request.method == "GET" and request.user.is_authenticated:
        # #This works:
        # text_content = "Hello World"
        # email = EmailMultiAlternatives('subject', text_content, 'Dont Reply <do_not_replay@domain.com>', ['bryan@gdprhero.io'])
        # email.send()
        
        # today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
        # today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)        
        print(datetime.date.today())
        todays_snippets = Snippet.objects.filter(created__contains=datetime.date.today()).values('app_id')
        print(todays_snippets)
        print(todays_snippets.count())
        allApps = Apps.objects.all().values_list('app_id', flat=True) 
        print(allApps)
        print(allApps.count())
        df = pd.DataFrame(list(Snippet.objects.filter(created__contains=datetime.date.today()).values()))
        allAppsToPandas = pd.DataFrame(list(Apps.objects.all().values()))
        allColumns = pd.merge(df, allAppsToPandas, how='left', on=['app_id'])
        allColumns.to_csv("/Users/bryanmarks/GDPRHero/allColumns.csv")
        mixpanelColumns = allColumns[allColumns['mixpanel_bool'] == True]
        mixpanelColumns.to_csv("/Users/bryanmarks/GDPRHero/mixpanelColumns.csv")
        # for oneSnippet in todays_snippets:
        #     print(type(oneSnippet))
        #     print(oneSnippet["app_id"])
        #     itemForReview = oneSnippet["app_id"]
        #     for itemForReview in allApps:
        #         print("allApps")
        #         appForEmail = Apps.objects.filter(app_id=allApps).values()[0]
        #         print(appForEmail)
                

        return render(request, 'app_home.html')
