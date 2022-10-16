from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
class LoginForm(AuthenticationForm):

	class Meta:
		model = User
		fields = '__all__'

class RegisterForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['username','password1','password2']
class UpdateAccountForm(UserChangeForm):

	class Meta:
		model = User
		fields = ['username']
class UpdateProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['bio','image']