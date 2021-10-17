# Develop a basic port scanner to check if particular ports are open or closed for
# an input remote host.
import socket

connect = socket.socket( )


# HOST = 'localhost'


def scanner(HOST, PORT):
    try:
        connect.connect(HOST, PORT)
        return True
    except:
        return False


server = input("Enter the server name\t")
PORT = input("enter the port number\t")

if not scanner(server, PORT):
    print('PORT NOT OPEN')
else:
    print('PORT IS OPEN!!!')
