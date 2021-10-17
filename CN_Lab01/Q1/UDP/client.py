import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host='localhost'
port=5000
client_socket.sendto(" ".encode(), (host, port))
data,addr=client_socket.recvfrom(1024)
print(str(data.decode()))