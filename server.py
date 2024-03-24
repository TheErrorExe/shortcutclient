#Made from TheErrorExe from GitHub
import http.server
import socketserver

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/4423':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><p>Correct</p></body></html>')
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><p>Incorrect</p></body></html>')

PORT = 4040

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print("Server ist running on", PORT)
    httpd.serve_forever()
