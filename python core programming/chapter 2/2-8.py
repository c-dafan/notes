from socketserver import (TCPServer as TCP,StreamRequestHandler as SRH)
from time import ctime

Host=''
Port=21567
Addr=(Host,Port)

class MyRequesHandler(SRH):
    def handle(self):
        print('... connected from:',self.client_address)
        self.wfile.write(('[%s] %s'%(ctime(),self.rfile.readline().decode())).encode())

tcpServ=TCP(Addr,MyRequesHandler)
print('waiting for connect')
tcpServ.serve_forever()