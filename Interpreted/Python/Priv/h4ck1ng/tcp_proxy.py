import sys
import socket
import threading


def server_loop(local_host, local_port, remote_host, remote_port, receive_first):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((local_host, local_port))
    except:
        print('[!! Failed to listen on {}:{}'.format(local_host, local_port))
        print('[!!] Check for other listening sockets or correct permissions.')
        sys.exit(0)

    print('[*] Listening on {}:{}'.format(local_host, local_port))
    server.listen(5)

    while True:
        client_socket, addr = server.accept()
        print('[==>] Received incoming connection from {}:{}'
              .format(addr[0], addr[1]))

        proxy_thread = threading.Thread(target=proxy_handler, args=(client_socket, remote_host, remote_port, receive_first))
        proxy_thread.start()


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('localhost')
    parser.add_argument('localport', type=int)
    parser.add_argument('remotehost')
    parser.add_argument('remoteport', type=int)
    parser.add_argument('-r', '--receive_first', action='store_true')

    args = parser.parse_args()

    local_host = args.localhost
    local_port = args.localport
    remote_host = args.remotehost
    remote_port = args.remoteport
    receive_first = args.receive_first

    server_loop(local_host, local_port, remote_host, remote_port, receive_first)


def proxy_handler(client_socket, remote_host, remote_port, receive_first):
    
    return 0


if __name__ == '__main__':
    main()
