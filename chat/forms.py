from django import forms
from .models import *
class RoomCreateForm(forms.ModelForm):

	class Meta:
		model = RoomChat
		fields = ['room_name']
		widgets= {
		'room_name':forms.TextInput(attrs={'class':'form-control'}),
		}

class MessageForm(forms.ModelForm):
	body = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control'}))
	class Meta:
		model= Message
		fields = ['body']
