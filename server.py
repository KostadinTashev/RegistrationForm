from http.server import HTTPServer, CGIHTTPRequestHandler

port = 8000

CGIHTTPRequestHandler.cgi_directories = ["/cgi-bin"]
server_address = ('', port)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
print(f"Server running on http://localhost:{port}/cgi-bin/register.py")
httpd.serve_forever()
