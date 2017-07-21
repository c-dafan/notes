from socket import *

Host='127.0.0.1'
Port=21567
Bufsize=1024
Addr=(Host,Port)

tcpclisock=socket(AF_INET,SOCK_STREAM)
tcpclisock.connect(Addr)

while True:
    data=input('> ')
    if not data:
        break
    
    # tcpclisock.send(('%s \r\n'%data).encode())
    tcpclisock.send(data.encode())
    data=tcpclisock.recv(Bufsize)
    if not data:
        break
    print(data.decode('utf-8'))
tcpclisock.close()