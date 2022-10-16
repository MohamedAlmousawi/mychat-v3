from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import datetime
# Create your models here.

class RoomChat(models.Model):
	room_name = models.CharField(max_length=100,unique=True)
	secret_key = models.CharField(max_length=16,null=True,blank=True)
	user = models.ManyToManyField(User,related_name='users')
	room_url = models.SlugField(max_length=100,null=True,blank=True)

	def save(self,*args,**kwargs):
		self.room_url=slugify(self.room_name) 
		super(RoomChat,self).save(*args,**kwargs)

	def __str__(self):
		return self.room_name

class Message(models.Model):
	user= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
	body = models.TextField()
	chat_channel = models.ForeignKey(RoomChat,on_delete=models.CASCADE)
	date= models.DateTimeField(default=datetime.now)

	def __str__(self):
		return str(self.user)