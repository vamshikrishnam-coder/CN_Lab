import socket
s=socket.socket()
s.bind(('localhost',8080))
s.listen()
data,addr=s.accept()
s.close()
