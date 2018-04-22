#! /usr/local/bin/python3

import socket
import threading

bind_ip = '0.0.0.0'
bind_port = 6969

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

print('[*] Listening on port {}:{}'.format(bind_ip, bind_port))


def handle_client(client_socket):
    request = client_socket.recv(4096)
    print('[*] Received {}'.format(request))
    client_socket.send(b'shit duck')
    client_socket.close()


while True:
    client, addr = server.accept()
    print('[*] Accepted connection from {} on port {}'.format(addr[0], addr[1]))

    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
