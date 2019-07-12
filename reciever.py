import sys
import os
import json
import socket

HOST = input('HOST: ')
PORT = 3702

reciever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
reciever.connect((HOST, PORT))

tree_count = reciever.recv(32)

for _ in tree_count:
    name_buffer = reciever.recv(32)
    name = reciever.recv(name_buffer)

    contents_buffer = reciever.recv(32)
    contents = reciever.recv(contents_buffer)

    with open(name, 'w') as file:
        file.write(contents)
