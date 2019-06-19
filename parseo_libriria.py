import numpy as np
import csv
import email
import os
directory = ".\\"
files = []

#Abrir archivo
f = open("correo.eml", "r")
mensaje = f.read()
f.close()


raw_content = email.message_from_string(mensaje)


if raw_content.is_multipart():
    for part in raw_content.walk():
        content_type = part.get_content_type()
        
        if content_type == 'text/plain':
            body = part.get_payload(decode=True)  # decode
            break
else:
	body = b.get_payload(decode=True)

print(body)