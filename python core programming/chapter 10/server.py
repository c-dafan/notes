from http.server import CGIHTTPRequestHandler,HTTPServer
from http.server import BaseHTTPRequestHandler,HTTPServer

def main():
    try:
        server=HTTPServer(('',80),CGIHTTPRequestHandler)
        print('welcome to the machine...'),
        print('press ^C once or twice to quit')
        server.serve_forever()
    except:
        print('^C received,shutting down server')
        server.socket.close()

if __name__=='__main__':
    main()