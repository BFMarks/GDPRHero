#log/forms.py
from django.contrib.auth.forms import AuthenticationForm 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from snippets.models import Snippet, Profile,InboundEmail

class SignUpForm(UserCreationForm):
    companyWebsite = forms.CharField(label="Company Website", max_length=30)
    username = forms.CharField(label="Company Name", max_length=30, 
                               widget=forms.TextInput(attrs={ 'name': 'username'}))


    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','companyWebsite')    
        # widgets = {
        #     'password1': forms.PasswordInput(),
        # }

    # def clean_email(self):
    # # Get the email
       #  email = self.cleaned_data.get('email')

       #  # Check to see if any users already exist with this email as a username.
	   #  try:
	   #      match = User.objects.get(email=email)
	   #  except User.DoesNotExist:
	   #      # Unable to find a user, this is fine
	   #      return email

	   #  # A user was found with this as a username, raise an error.
	   #  raise forms.ValidationError('This email address is already in use.')

class ProfileSignUpForm(forms.ModelForm):
    companyName = forms.CharField(max_length=100)
    companyWebsite = forms.CharField(max_length=100)

    class Meta:
        model = Profile
        fields = ('companyName', 'companyWebsite',)    

#Working
class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Company Name", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'password'}))

class HomeInput(forms.ModelForm):
    inputEmailToSpeakWithExpert = forms.CharField(max_length=100)

    class Meta:
        model = InboundEmail
        fields = ('inputEmailToSpeakWithExpert','properEmail','emailSentToUS',)  