
import socket
port = 5000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("localhost", port))
print("waiting on port:", port)
data, addr = server_socket.recvfrom(1024)
reply='hello buddy welcome to server'
print('connected to -> ' ,addr)
server_socket.sendto(reply.encode(),addr)
server_socket.close()
