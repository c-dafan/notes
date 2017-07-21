from socket import *

Host='127.0.0.1'
Port=21567
Bufsize=1024
Addr=(Host,Port)



while True:
    tcpclisock=socket(AF_INET,SOCK_STREAM)
    tcpclisock.connect(Addr)    
    data=input('> ')
    if not data:
        break
    tcpclisock.send(('%s \r\n'%data).encode())
    data=tcpclisock.recv(Bufsize)
    if not data:
        break   
    print(data.decode())
    tcpclisock.close()