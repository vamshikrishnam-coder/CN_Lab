# Using TCP socket, implement HTTP server and client
import socket
from socket import AF_INET, SOCK_STREAM, SO_REUSEADDR, SOL_SOCKET

# HTTP SERVER CREATION
HOST, PORT = 'localhost', 8081
response = b"HTTP/1.1 200 OK \n\nhello buddy welcome to server"
# HTTP SERVER END

server_socket = socket.socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
while True:
    try:
        client_socket, addr = server_socket.accept()
        print(client_socket.recv(1024).decode('utf-8'))
        client_socket.sendall(response)
        client_socket.close()
    except Exception as e:
        print(e)
socketserver.close()
