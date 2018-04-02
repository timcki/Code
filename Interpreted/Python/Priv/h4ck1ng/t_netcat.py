#! /usr/local/bin/python3

import socket
import threading
import subprocess
from sys import stdin
import argparse

listen = False
command = False
upload = False
execute = ''
target = ''
upload_destination = ''
port = 0


def main():
    global target
    global port
    global upload_destination
    global execute
    global listen
    global command
    global upload

    parser = argparse.ArgumentParser(description='My net tool')
    parser.add_argument('-t', '--target', help='Set the target ip')
    parser.add_argument('-p', '--port', help='Set the target port', type=int)
    parser.add_argument(
        '-l', '--listen', help='Listen on [host]:[port] for incomming connections', action='store_true')
    parser.add_argument('-c', '--command',
                        help='Initialize a command', action='store_true')
    parser.add_argument(
        '-e', '--execute', help='Execute the given file upon receiving a coonection')
    parser.add_argument(
        '-u', '--upload', help='Upon receiving connection upload a file and write to [destination]')
    args = parser.parse_args()

    target = args.target
    port = args.port
    upload_destination = args.upload
    execute = args.execute
    listen = args.listen
    command = args.command
    upload = args.upload

    if not listen and target and port > 0:
        buffer = stdin.readline()
        client_sender(buffer)
    else:
        server_loop()


def client_sender(buffer):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((target, port))
        if len(buffer):
            client.send(buffer.encode('utf-8'))

        while True:
            recv_len = 1
            response = bytes()

            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data

                if recv_len < 4096:
                    break

            print(response.decode('utf-8'), end=' ')
            buffer = input()
            buffer += '\n'
            client.send(buffer.encode(encoding='utf_8', errors='strict'))

    except:
        print('[*] Exception! Exiting.')
        client.close()


def server_loop():
    global target

    if not target:
        target = '0.0.0.0'

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target, port))
    server.listen(5)

    while True:
        client_socket, addr = server.accept()
        print('[*] Accepted connection from {} on port {}'.format(addr[0], addr[1]))

        client_thread = threading.Thread(
            target=client_handler, args=(client_socket,))
        client_thread.start()


def run_command(command):
    command = command.strip()

    try:
        output = subprocess.check_output(
            command, stderr=subprocess.STDOUT, shell=True)
    except:
        output = 'Failed to execute command.\r\n'.encode(
            encoding='utf_8', errors='strict')

    return output


def client_handler(client_socket):
    global upload
    global execute
    global command

    if upload_destination:
        file_buffer = ''

        while True:
            data = client_socket.recv(1024)
            if not len(data):
                break
            else:
                file_buffer += data
        try:
            file_descriptor = open(upload_destination, 'wb')
            file_descriptor.write(file_buffer)
            file_descriptor.close()

            client_socket.send('Successfully saved file to {}\r\n'.format(
                upload_destination).encode(encoding='utf_8', errors='strict'))
        except:
            client_socket.send('Failed to send file to {}\r\n'.format(
                upload_destination).encode(encoding='utf_8', errors='strict'))

    if execute:
        output = run_command(execute)
        client_socket.send(output)

    if command:
        while True:
            client_socket.send('<ASS:#>'.encode(
                encoding='utf_8', errors='strict'))
            cmd_buffer = ''
            while '\n' not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024).decode('utf-8')

            response = run_command(cmd_buffer)
            client_socket.send(response)


if __name__ == '__main__':
    main()
