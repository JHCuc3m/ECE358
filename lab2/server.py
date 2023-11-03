import socket
import os
import mimetypes
from datetime import datetime
from email.utils import formatdate

# Define the server IP address and port
SERVER_ADDRESS = ('127.0.0.1', 6789)

# Define the document root directory where your files are stored
DOCUMENT_ROOT = "./"  # Update this to the path of your server directory

# Function to handle a single HTTP request
def handle_request(client_socket):
    data = client_socket.recv(1024).decode('utf-8')

    if not data:
        return

    request_method, path, _ = data.split(' ', 2)
    if request_method == 'GET' or request_method == 'HEAD':
        file_path = DOCUMENT_ROOT + path

        if os.path.exists(file_path) and os.path.isfile(file_path):
            content_type, _ = mimetypes.guess_type(file_path)
            file_size = os.path.getsize(file_path)
            last_modified = formatdate(os.path.getmtime(file_path), usegmt=True)

            response_headers = [
                'HTTP/1.1 200 OK',
                f'Connection: close',
                f'Date: {formatdate(timeval=None, localtime=False, usegmt=True)}',
                f'Server: SimplePythonServer',
                f'Last-Modified: {last_modified}',
                f'Content-Length: {file_size}',
                f'Content-Type: {content_type}',
                '\r\n',
            ]

            response = '\r\n'.join(response_headers)

            if request_method == 'GET':
                with open(file_path, 'rb') as file:
                    response += file.read().decode('utf-8')

            client_socket.send(response.encode('utf-8'))
        else:
            not_found_response = 'HTTP/1.1 404 Not Found\r\n\r\n<h1>404 Not Found</h1>'
            client_socket.send(not_found_response.encode('utf-8'))

    client_socket.close()

# Create a socket to listen for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(SERVER_ADDRESS)
server_socket.listen(1)

print(f"Server is listening on {SERVER_ADDRESS[0]}:{SERVER_ADDRESS[1]}")

while True:
    client_socket, client_address = server_socket.accept()
    handle_request(client_socket)
