from http.server import BaseHTTPRequestHandler,HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        try:
            f=open('index.html','rb')
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write(f.read())
        except IOError:
            self.send_error(404,'File Not Fount:%s'%self.path)

def main():
    try:
        server=HTTPServer(('',80),MyHandler)
        print('welcome to the machine...'),
        print('press ^C once or twice to quit')
        server.serve_forever()
    except:
        print('^C received,shutting down server')
        server.socket.close()

if __name__=='__main__':
    main()