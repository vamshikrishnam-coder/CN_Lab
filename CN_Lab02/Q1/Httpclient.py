# Using TCP socket, implement HTTP server and client.
import socket
from socket import AF_INET, SOCK_STREAM, SO_REUSEADDR, SOL_SOCKET

client_socket = socket.socket(AF_INET, SOCK_STREAM)
HOST, PORT = 'localhost', 8081
# REQUEST SENT TO SERVER
request = f"GET /HTTP/1.1\r\n: {HOST}:{PORT}\r\n\r\n".encode('utf8')
client_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
client_socket.connect((HOST, PORT))
client_socket.sendall(request)
response = ""
while True:
    data = client_socket.recv(1024)
    if data == b'':
        break
    print(data.decode())
client_socket.close()
