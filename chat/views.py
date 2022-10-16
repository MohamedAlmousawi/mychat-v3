from django.shortcuts import render,redirect
from django.urls import reverse,reverse_lazy
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .test import *
from django.contrib import messages
from .encrypt import encryption_text,dencryption_text
# Create your views here.
@login_required
def HomeView(request):
	username= request.user
	if request.method =="POST":
		room_name=request.POST.get('room_name')
		secret_key=request.POST.get('secret_key')

		if RoomChat.objects.filter(room_name=room_name,secret_key=secret_key).exists():
			roomchat=RoomChat.objects.get(room_name=room_name)
			roomchat.user.add(User.objects.get(id=request.user.id))
			return redirect(reverse('chat',args=[roomchat.id]))
		else:
			messages.info(request,'Incorrect Chat Name or Secret Key.')
	context = {
		
	}
	return render(request,'pages/home.html',context)
@login_required
def ChatView(request,id):
	chat =RoomChat.objects.get(id=id)
	messages =  Message.objects.filter(chat_channel=chat)
	if request.method == "POST":
		form= MessageForm(request.POST)
		if form.is_valid():
			myform =form.save(commit=False)
			myform.user= request.user
			myform.body =encryption_text(myform.body)
			myform.chat_channel=chat
			myform.save()
			return redirect(reverse('chat',args=[chat.id]))

	else:
		form=MessageForm()
	if 'leave' in request.GET:
		chat.user.remove(request.user)
		return redirect(reverse('home'))
	context={
	'chat':chat,
	'form':form,
	'chat_messages':messages
	}

	return render(request,'chat.html',context)

def DeleteChatView(request,pk,id):
	message= Message.objects.get(id=id)
	if request.user.id == message.user.id:
		if request.method == "POST":
			message.delete()
	return HttpResponseRedirect(reverse('chat',args=[pk]))

def EditChatView(request,pk,id):
	message= Message.objects.get(id=id)
	en= dencryption_text(message.body)
	if request.method == 'POST':
		message.body=encryption_text(request.POST.get('body'))
		message.save()
		return redirect(reverse('chat',args=[pk]))
	context = {
	'en':en,
	'message':message,
	}
	return render(request,'pages/edit_message.html',context)


def CreateChatView(request):
	if request.method =='POST':
		form= RoomCreateForm(request.POST)
		if form.is_valid():
			myform =form.save(commit=False)
			myform.secret_key=secret_key_generate()
			myform.save()
			myform.user.add(User.objects.get(id=request.user.id))
			return redirect(reverse('chat',args=[myform.pk]))
	else:
		form = RoomCreateForm()

	context={
		'form':form,
	}
	return render(request,'pages/create_chat.html',context)