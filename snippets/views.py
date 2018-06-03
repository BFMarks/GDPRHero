from snippets.models import Snippet, Profile
from account.models import Apps, AppsFlyerResponse
from snippets.serializers import SnippetSerializer,ProfileSerializer, AppsSerializer, AppsFlyerResponseSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from snippets.serializers import UserSerializer
from rest_framework import permissions,authentication
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required




class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # remove permissions for public
    # permission_classes = (permissions.IsAdminUser,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class AppsList(generics.ListCreateAPIView):
    queryset = Apps.objects.all()
    serializer_class = AppsSerializer
    # remove permissions for public
    # permission_classes = (permissions.IsAdminUser,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    # permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # remove permissions for public
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)        

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # remove permissions for public
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # remove permissions for public
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)

class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AppsFlyerResponseList(generics.RetrieveAPIView):
    queryset = AppsFlyerResponse.objects.all()
    serializer_class = AppsFlyerResponseSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class ScrubbedUserList(generics.ListAPIView):
#     serializer_class = ScrubbedUserSerializer

#     def get_queryset(self):
#         """
#         This view should return a list of all the purchases
#         for the currently authenticated user.
#         """
#         user = self.request.user
#         return Purchase.objects.filter(purchaser=user)


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'snippets': reverse('snippet-list', request=request, format=format),
#         'profile': reverse('profile-list', request=request, format=format)
#     })









