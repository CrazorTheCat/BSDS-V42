import http.server
import os
import socketserver
import socket

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler
os.chdir("Update")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Server is ready")
    httpd.serve_forever()
