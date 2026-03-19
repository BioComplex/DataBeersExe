import http.server
import socketserver

PORT = 8766
DIRECTORY = "/Users/rmenezes/Documents/Conference Organization/DataBeers/Site"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    def log_message(self, format, *args):
        pass  # suppress output

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving on http://localhost:{PORT}", flush=True)
    httpd.serve_forever()
