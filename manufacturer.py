#!/usr/bin/python3.6

import datetime
import socket
import time
import uuid

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

# for simplicity the variable will simulate a public key, but no public/private
# key pairs are actually used in this demo
PUBLIC_KEY = "1234-VW-Group"

block = {
    "timestamp": time.ctime(),
    "car": {
        "id": str(uuid.uuid4()),
        "manufacturer": "Volkswagen",
        "model": "Golf",
        "mileage": 0,
        "year": str(datetime.datetime.today().year),
        "country_of_origin": "Czech Republic",
        "owner": PUBLIC_KEY
    },
    "id": PUBLIC_KEY
}

# send the block to the network
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # in python3 the string must be encoded
    s.sendall(str(block).encode())
    data = s.recv(1024)

print('The block has been received by the network.')

