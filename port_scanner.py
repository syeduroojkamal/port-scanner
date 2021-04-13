import socket
from IPy import IP

ipaddress = input('[+] Enter Target to scan: ')
port = 80

try:
    sock = socket.socket()
    sock.connect((ipaddress, port))
except:
    print('[-] port 80 is closed')