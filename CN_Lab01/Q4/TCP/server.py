import socket
import threading
server_socket =socket.socket()
host='localhost'
port=8089
server_socket.bind((host, port))
server_socket.listen()
clients=[]
names=[]
## this is to send message to all
def sendtoall(message,client):
    for c in clients:
        if(c!=client):
            c.send(message)
# this is handle clints connections , receive message from clients
def client_manage(client):
    while True:
        try:
            message=client.recv(1024)
            sendtoall(message,client)
        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            name=names[index]
            sendtoall(f'{name} has left the chatroom'.encode('utf-8'),client)
            names.remove(name)
            break
#establish the client connections
def receive():
    while  True:
        print('Waiting on port ', port)
        client,addr=server_socket.accept()
        print('connected to ->',addr)
        client.send('Enter the name ->'.encode('utf-8'))
        Name=client.recv(1024).decode('utf-8')
        print(f'Client Name -> {Name}')
        names.append(Name)
        clients.append(client)
        sendtoall(f'{Name} has entered the chatroom'.encode('utf-8'),client)
        client.send('welcome'.encode('utf-8'))
        thread=threading.Thread(target=client_manage, args=(client,))
        thread.start()
if __name__ == '__main__':
    receive()



