#importing
import random
import string

def secret_key_generate():
    chars=string.digits+string.ascii_letters
    secret_key= ''
    for i in range(random.randint(10,15)):
        char = random.choice(chars)
        secret_key+=char
    return secret_key

