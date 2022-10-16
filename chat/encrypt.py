import string
enc_chars= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 "
denc_chars="bcdefghijklmnopqrstuvwxyzaBCDEFGHIJKLMNOPQRSTUVWXYZA1234567890 "

def encryption_text(text):
    enc_text= ''
    for char in text:
        if char not in enc_chars:
            enc_text+=char
        else:
            index = enc_chars.index(char)
            enc_text +=denc_chars[index]
    return enc_text




def dencryption_text(text):
    enc_text= ''
    for char in text:
        if char not in enc_chars:
            enc_text+=char
        else:
            index = denc_chars.index(char)
            enc_text +=enc_chars[index]
    return enc_text



