import http.server
import socketserver

port = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), Handler) as httpd:
    print("Server start!\nPort: ", port)
    print("http://localhost:8080/")
    httpd.serve_forever()
