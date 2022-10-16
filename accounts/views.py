from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
class LoginChatView(LoginView):
	model= User
	template_name= 'pages/login.html'
	form_class = LoginForm

def RegisterChatView(request):

	if request.method == "POST":
		form= RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username=request.POST.get('username')
			password=request.POST.get('password1')
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect(reverse('home'))
	else:
		form= RegisterForm()
	context= {
	'form':form
	}
	return render(request,'pages/register.html',context)

class LogoutChatView(LogoutView):
	model =User
	template_name= 'pages/logout.html'
login_required
@login_required
def UpdateAccountView(request):
	profile = Profile.objects.get(user=request.user.id)
	if request.method == "POST":
		form1= UpdateAccountForm(request.POST,instance=request.user)
		form2 = UpdateProfileForm(request.POST,request.FILES,instance=profile)
		if form1.is_valid() and form2.is_valid():
			form1.save()
			form2.save()
			return redirect(reverse('profile',args=[request.user.id]))
	else:
		form1 = UpdateAccountForm(instance=request.user)
		form2 = UpdateProfileForm(instance=profile)
	context = {
	'form1':form1,
	'form2':form2
	}
	return render(request,'pages/edit_profile.html',context)

def AccountView(request,id):
	profile = Profile.objects.get(user=id)
	context = {
	'profile':profile
	}
	return render(request,'pages/profile.html',context)

