#!/usr/bin/python3.6


import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

block = {
    "timestamp": "time",
    "data": "some data here"
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # in python3 the string must be encoded
    s.sendall(str(block).encode())
    data = s.recv(1024)

print('Received', repr(data.decode()))

