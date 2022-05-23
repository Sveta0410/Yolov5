import os
from http.server import HTTPServer, CGIHTTPRequestHandler
#  os.chdir('gstr')
os.chdir('templates')

# Create server object listening the port 8080
server_object = HTTPServer(server_address=('', 8080), RequestHandlerClass=CGIHTTPRequestHandler)
# Start the web server
server_object.serve_forever()
