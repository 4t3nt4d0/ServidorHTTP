#Usar a porta 80

import SimpleHTTPServer
import SocketServer

PORT = 400
 
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("192.168.2.101", PORT), Handler)
 
print "servidor web na porta", PORT
httpd.serve_forever()
