import socket
server_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost',9997))
while True:
    d=server_socket.recvfrom(1024)
    data=d[0]
    addr=d[1]
    print("client message->",str(data.decode()))
    reply=input('enter the message')
    server_socket.sendto(reply.encode(),addr)
server_socket.close()