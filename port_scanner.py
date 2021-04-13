import socket
from IPy import IP

ipaddress = input('[+] Enter Target to Scan: ')
port = 80

try:
    sock = socket.socket()
    sock.connect((ipaddress, port))
    print('[+] Port 80 is Open')
except:
    print('[-] Port 80 is Closed')
    
# ip of mozilla for testing 104.18.165.34
