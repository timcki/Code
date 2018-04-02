#! /usr/local/bin/python3

import socket

target_host = "127.0.0.1"
target_port = 6969

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

client.send(b'It\'s me bitch')
response = client.recv(4096)

for phrase in str(response).split('\\n'):
    print(phrase)
