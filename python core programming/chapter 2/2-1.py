from socket import *
from time import ctime

Host=''
Port=21567
Bufsize=1024
Addr=(Host,Port)

tcpSersock=socket(AF_INET,SOCK_STREAM)
tcpSersock.bind(Addr)
tcpSersock.listen(5)

while True:
    print('waiting for connection')
    tcpclisock,addr=tcpSersock.accept()
    print('--- connect from:',addr)
    while True:
        data=tcpclisock.recv(Bufsize)
        if not data:
            break
        # '[%s] %s'%(bytes(ctime(),'utf-8'),data)
        tcpclisock.send(b'[%s] %s'%(bytes(ctime(),'utf-8'),data))
    tcpclisock.close()
tcpSersock.close()