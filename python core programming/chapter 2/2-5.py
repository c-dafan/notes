from socket import *
from time import ctime

Host=''
Port=21567
Bufsize=1024
Addr=(Host,Port)

udpsersock=socket(AF_INET,SOCK_DGRAM)
udpsersock.bind(Addr)

while True:
    print('waiting for message ')
    data,addr=udpsersock.recvfrom(Bufsize)
    print('from:',addr)
    udpsersock.sendto(b'[%s] %s'%(bytes(ctime(),'utf-8'),data),addr)

udpsersock.close()