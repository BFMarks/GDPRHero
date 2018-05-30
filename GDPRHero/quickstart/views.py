# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from GDPRHero.quickstart.serializers import UserSerializer, GroupSerializer
from django.template import loader
from django.http import HttpResponse
from rest_framework.authtoken.models import Token
# import pandas as pd
import datetime
from snippets.models import Snippet
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect
# from .forms import GenerateRandomUserForm
# from .tasks import create_random_user_accounts


# class UsersListView(ListView):
#     template_name = 'users_list.html'
#     model = User


# class GenerateRandomUserView(FormView):
#     template_name = 'generate_random_users.html'
#     form_class = GenerateRandomUserForm

    # def form_valid(self, form):
    #     total = form.cleaned_data.get('total')
    #     create_random_user_accounts.delay(total)
    #     messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
    #     return redirect('users_list')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


def documentation(request): 
    if request.user.is_authenticated:
        token = Token.objects.filter(user=request.user)
        actualTokenString = list(token)[0]
        print(actualTokenString)
        return render(request, 'documentation.html', {
            'actualTokenString': actualTokenString,
            })
    else:
        return render(request, 'documentation.html')

