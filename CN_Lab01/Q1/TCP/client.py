import  socket 
client_socket= socket.socket()
client_socket.connect(('localhost',5003))
print(client_socket.recv(1024).decode('utf8'))
client_socket.close()