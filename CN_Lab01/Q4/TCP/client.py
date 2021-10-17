import socket
import threading
name=input('enter ur name \t')
client_socket=socket.socket()
client_socket.connect(('localhost',8089))
def receive():
    while True:
        try:
            message=client_socket.recv(1024).decode('utf-8')
            if message=='Enter the name ->':
                client_socket.send(name.encode('utf-8'))
            else:
                print(message)
        except:
            print('error')
            client_socket.close()
def send():
    while True:
        message=f'{name}-> {input()}'
        client_socket.send(message.encode())
receive_thread=threading.Thread(target=receive)
receive_thread.start()
send_thread=threading.Thread(target=send)
send_thread.start()