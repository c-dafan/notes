from socket import *

Host='127.0.0.1'
Port=21567
Bufsize=1024
Addr=(Host,Port)

udpserSock=socket(AF_INET,SOCK_DGRAM)
while True:
    data=input('> ')
    if not data:
        break
    udpserSock.sendto(data.encode(),Addr)
    data,addr=udpserSock.recvfrom(Bufsize)
    if not data:
        break
    print(data.decode())