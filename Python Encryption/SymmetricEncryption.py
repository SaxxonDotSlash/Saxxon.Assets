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
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))

print(key)
print("First level SHA ecnryption success!")