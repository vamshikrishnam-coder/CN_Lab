import socket
client_socket=socket.socket()
client_socket.connect(('localhost',9995))
data=input('enter the message & enter "bye" to end')
while data.strip()!='bye':
    client_socket.send(data.encode())
    msg = client_socket.recv(1024).decode()
    print('server message\t',str(msg))
    data=input('enter the message')
client_socket.close()



