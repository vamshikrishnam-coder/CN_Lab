# Write a program to translate a Domain name or hostname to its IP address
# and vice versa
import socket


def get_domain():
    ip = input('enter the ip address\t')
    try:
        domain = socket.gethostbyaddr(ip)
        print('the domain address is ->', domain[0])
    except socket.error as err:
        print("invalid ip address")


def get_ip():
    domain = input('enter the domain name\t')
    try:
        ip = socket.gethostbyname(str(domain))
        print("the ip is ->", ip)
    except socket.gaierror as err:
        print("invalid domain name , error", err)


get_ip()
get_domain()

