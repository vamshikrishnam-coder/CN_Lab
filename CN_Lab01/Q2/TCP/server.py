import socket
from datetime import date
server_socket = socket.socket()
server_socket.bind(('localhost',9993))
server_socket.listen(1)
client_socket,addr=server_socket.accept()
print('connected to -> ',addr)
s=client_socket.recv(1024).decode()
client_socket.send(bytes(str(date.today()).encode()))
server_socket.close()

