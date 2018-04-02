import threading
import paramiko
import socket
import sys


host_key = paramiko.RSAKey(filename='id_rsa')


class Server(paramiko.ServerInterface):

    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        if username == 'root' and password == 'toor':
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED

try:
    sock = socket.socket(type=socket.SOCK_STREAM, family=socket.AF_INET)
    sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 34))
    sock.listen(100)
    print('[+] Listening for connection ...')
    client, addr = sock.accept()
except Exception as e:
    print('[-] Listen/bind/accept failed: {}'.format(e))
    sys.exit(1)
print('[+] Got a connection!')

try:
    t = paramiko.Transport(client)
    try:
        t.load_server_moduli()
    except:
        print('[-] Failed to load moduli -- gex will be unsuported.')
        raise

    t.add_server_key(host_key)
    server = Server()
    try:
        t.start_server(server=server)
    except paramiko.SSHException:
        print('[-] SSH negotiation failed.')

    chan = t.accept(20)
    print('[+] Authenticated')
    print(chan.recv(1024))
    chan.send('Yeah i can see that.')

except Exception as e:
    print('[-] Caught exception: {}: {}'.format(e.__class__, str(e)))
    try:
        t.close()
    except:
        pass
    sys.exit(1)
