import http.server
import socketserver

port = input("Port:")
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", port), Handler) as httpd:
    print("Server start!\nPort: ", port)
    print(f"http://localhost:{port}/")
    httpd.serve_forever()
