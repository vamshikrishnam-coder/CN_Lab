import socket
server_socket=socket.socket()
server_socket.bind(('localhost',9995))
server_socket.listen(1)
client_socket,addr=server_socket.accept()
print('connected to ->',addr)
while True:
    msg=client_socket.recv(1024).decode()
    print('client message\t',str(msg))
    if not msg:
        break
    data=input('enter the message')
    client_socket.send(data.encode())
server_socket.close()