###Note:
### = The heading of a section of code
## = Terminal or outside of IDE instructions
# = A traditional comment


#Im just going to hard code each translator, rather than import the code like I was planning.

###Symmetric Encryption###
##Run 'python -m pip install cryptography'

import base64
import os
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#input feild for custom password
password_provided = input("Enter an encryption key: ")
#encodes the password
password = password_provided.encode()
salt = b'UnguessableCode'
encrypt = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(encrypt.derive(password))

print(key)
print("Your encryption key is above.")

OriginalMSG= input("Enter your message: ")
#inputs unencrypted message into the encoder
message_provided = OriginalMSG
#encodes the message
message = message_provided.encode()
salt = key
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
encrypted_message = base64.urlsafe_b64encode(kdf.derive(message))
print(encrypted_message)
print("First level SHA256 ecnryption success!")



###Translators###
#We need to take the string translation and run it through each of these in order, while encrypting it in between each layer.
 
###Binary Translator###


###Hex Translator###


###Octal Translator###


###String Splitter###
#Splits each string of characters into a list and applies ASCII values to them

