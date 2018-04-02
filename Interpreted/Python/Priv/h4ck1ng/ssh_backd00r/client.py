import paramiko
import threading

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('127.0.0.1', port=34, username='root', password='toor')
chan = client.get_transport().open_session()
chan.send('Hey i am connected maboi #_#')
print(chan.recv(1024))
client.close()
