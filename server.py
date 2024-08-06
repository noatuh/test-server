import http.server
import socketserver

# Define the handler to serve files from the current directory
Handler = http.server.SimpleHTTPRequestHandler

# Set the server's port
PORT = 8080

# Create a TCPServer object to listen on the specified port
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    # Handle requests until an explicit shutdown
    httpd.serve_forever()
