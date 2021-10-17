import socket
from datetime import date
client_socket = socket.socket()
client_socket.connect(('localhost',9993))
client_socket.send(bytes('what is the date today','utf-8'))
print("present day date",client_socket.recv(1024).decode())
client_socket.close()