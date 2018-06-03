# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from log.forms import  ProfileSignUpForm, HomeInput,SignUpForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from snippets.models import Snippet, Profile,InboundEmail
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail

# Create your views here.
# @login_required(login_url="login/")
def home(request):
    if request.method == 'GET':
        properEmail =""
        # if request.user.is_authenticated():
            # return redirect('account')

    if request.method == 'POST':
        homeInput_form = HomeInput(data=request.POST)
        if homeInput_form.is_valid():
            subject = homeInput_form.cleaned_data['inputEmailToSpeakWithExpert']
            # Send a text or email
            # print(subject)
            try:
                validate_email(subject)
            except ValidationError as e:
                properEmail = "Please enter a valid email."
                # messages.error(request, "Error")
                print(properEmail)
                return render(request, 'home.html', {
                    'properEmail': properEmail
                })
            else:
                print("hooray! email is valid")
                instance = InboundEmail.objects.create(inboundEmail=subject)
                properEmail = "We will reach out to you shortly."
                return render(request, 'home.html', {
                    'properEmail': properEmail
                })
    else:
        homeInput_form = HomeInput()
    return render(request, 'home.html', {
        'homeInput_form': homeInput_form
    })

def newHome(request):
    if request.method == 'GET':
        properEmail =""
        # if request.user.is_authenticated():
            # return redirect('account')

    if request.method == 'POST':
        homeInput_form = HomeInput(data=request.POST)
        if homeInput_form.is_valid():
            subject = homeInput_form.cleaned_data['inputEmailToSpeakWithExpert']
            # Send a text or email
            # print(subject)
            try:
                validate_email(subject)
            except ValidationError as e:
                properEmail = "Please enter a valid email."
                # messages.error(request, "Error")
                print(properEmail)
                return render(request, 'home.html', {
                    'properEmail': properEmail
                })
            else:
                print("hooray! email is valid")
                instance = InboundEmail.objects.create(inboundEmail=subject)
                properEmail = "We will reach out to you shortly."
                return render(request, 'home.html', {
                    'properEmail': properEmail
                })
    else:
        homeInput_form = HomeInput()
    return render(request, 'newHome.html', {
        'homeInput_form': homeInput_form
    })

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("test")
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('companyWebsite')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('app_list')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
    

def loginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print("test")
            user = form.get_user()
            login(request,user)
            return redirect('app_list')
    else:
        form = AuthenticationForm()
    return render(request,'login.html',{'form':form})


def termsofservice(request):
    return render(request,'termsofservice.html')