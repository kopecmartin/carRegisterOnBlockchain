#!/usr/bin/python3.6


import sys
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


if len(sys.argv) != 2:
    print("Provide ID of a car!")
    sys.exit(1)

block = {
    "request": "history",
    "car_id": sys.argv[1]
}

# send the block to the network
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # in python3 the string must be encoded
    s.sendall(str(block).encode())
    data = s.recv(1024)

print('The block has been received by the network.', repr(data.decode()))

