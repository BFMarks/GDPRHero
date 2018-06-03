from rest_framework import serializers
from snippets.models import Snippet, Profile
from account.models import Apps
from django.contrib.auth.models import User

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'id','app_id', 'owner','bundle_id',
                  'deviceName', 'advertising_id', 'idfa','mixpanel_user_id','customer_user_id','amplitude_user_id','braze_user_id',
'mixpanel_user_id',
'urbanairship_user_id',
'branch_user_id',
'adjust_user_id',
'customer_user_id',
'app_id',
'optimizely_user_id',
'googleAnalytics_user_id',
'facebook_user_id',
'clever_tap_user_id',
'fabric_user_id',
'subparam1_user_id',
'subparam2_user_id',
'subparam3_user_id','created')
        

class AppsSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Apps
        fields = ('url', 'id','app_id', 'owner','bundle_id',
                  'id','appsflyer_api_key','amplitude_api_key', 'appsflyer_bool', 'created')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)
    profile = serializers.HyperlinkedRelatedField(many=False, view_name='profile-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'snippets', 'profile')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    # highlight = serializers.HyperlinkedIdentityField(view_name='profile-highlight', format='html')

    class Meta:
        model = Profile
        fields = ('url', 'id','companyName','companyWebsite','email', 'user')
            # , 'owner','bundle_id',
            #       'deviceName', 'advertising_id', 'idfa', 'appsflyer_int',)        

class AppsFlyerResponseSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Snippet
        fields = ('created', 'subject_request_id','received_time', 'expected_completion_time','encoded_request')
             
# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#       Update and return an existing `Snippet` instance, given the validated data.

#       CHANGE INSTANCE NAMES
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance