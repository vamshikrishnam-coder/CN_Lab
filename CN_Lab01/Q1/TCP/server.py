import  socket 
server_socket = socket.socket()
server_socket.bind(('localhost',5003))
server_socket.listen(1)
client_socket,addr=server_socket.accept()
print('connected with -> ' ,addr)
client_socket.send(bytes('Hello buddy welcome to server','utf-8'))
server_socket.close()
