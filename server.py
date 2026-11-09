#!/usr/bin/env python3
"""
STARCOMP PC CONFIGURATOR LOCAL WEB SERVER
Lightweight HTTP Server for Local Marketing Team Usage
"""

import http.server
import socketserver
import os
import sys

PORT = 3000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Enable CORS and disable cache during local usage
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else PORT
    # Try port or increment if busy
    for p in range(port, port + 20):
        try:
            with socketserver.TCPServer(("", p), Handler) as httpd:
                print(f"STARCOMP PC Configurator berjalan di: http://localhost:{p}")
                print(f"Direktori root: {DIRECTORY}")
                print("Tekan Ctrl+C untuk berhenti.")
                httpd.serve_forever()
        except OSError:
            continue
