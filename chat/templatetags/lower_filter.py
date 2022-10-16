from django import template
from ..models import RoomChat
register = template.Library()
  
@register.filter()
def dencryption_text(text):
    enc_chars= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
    denc_chars="bcdefghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZA1234567890 "
    enc_text= ''
    for char in text:
        if char not in enc_chars:
            enc_text+=char
        else:
            index = denc_chars.index(char)
            enc_text +=enc_chars[index]
    return enc_text

@register.filter()
def checking(id,id2):

    chat =RoomChat.objects.get(id=id)
    boolean = False
	# if chat.user.filter(id=user.id):
    if chat.user.filter(id=id2):
        boolean=True
    return boolean