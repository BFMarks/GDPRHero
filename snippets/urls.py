from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

# API endpoints
urlpatterns = format_suffix_patterns([


    url(r'^snippets/$',
        views.SnippetList.as_view(),
        name='snippet-list'),

    url(r'^profile/$',
        views.ProfileList.as_view(),
        name='profile-list'),

    url(r'^profile/(?P<pk>[0-9]+)/$',
        views.ProfileDetail.as_view(),
        name='profile-detail'),

    url(r'^snippets/(?P<pk>[0-9]+)/$',
        views.SnippetDetail.as_view(),
        name='snippet-detail'),

    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
        views.SnippetHighlight.as_view(),
        name='snippet-highlight'),

    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),

    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail'),

    url(r'^apps/$',
        views.AppsList.as_view(),
        name='apps-list'),

    url(r'^apps/(?P<pk>[0-9]+)/$',
        views.AppsList.as_view(),
        name='apps-detail'),

    # url(r'^appsflyerResponse/$',
    #     views.AppsFlyerResponseList.as_view(),
    #     name='AppsFlyerResponse-list'),

    # url('^ScrubbedUserList/(?P<username>.+)/$', ScrubbedUserList.as_view()),
])
