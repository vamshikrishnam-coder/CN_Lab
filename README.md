# CNLAB_0-5

# CN_lab01
Lab Assignment I

1) Create a TCP/IP client-server program in which a single client connects to the server. 
The server then should send a greeting to the client. Repeat the experiment using 
UDP.
2) Create a TCP/IP client-server program. The client should send a message asking for the 
current date. The server should respond with the current date that will be displayed on 
the client.
3) Create a TCP/IP server-client program in which both client and server can send and 
receive messages (Chat application). Repeat the experiment using UDP.
4) Create a chat room such that multiple clients can connect to a server. The clients must 
be able to both send and receive messages to each other via the server. Create chat 
rooms using TCP and UDP


## CN_LAB02
References:
1. https://www.geeksforgeeks.org/what-is-web-socket-and-how-it-is-different-from-the-http/
2. http://www2.cs.uh.edu/~gnawali/courses/cosc6377-f12/p1/http.html
3. https://www.geeksforgeeks.org/domain-name-system-dns-in-application-layer/
4. https://www.youtube.com/watch?v=lb1Dw0elw0Q – Wireshark
5. https://www.youtube.com/watch?v=jL4uJfCzBA4


1. Using TCP socket, implement HTTP server and client.
2. Write a program to translate a Domain name or hostname to its IP address
and vice versa
3. Develop a program to view the data of top 50 movies in IMDB. (Movie name,
actors, IMDB ratings)
4. Write a program to display the details of an input URL (status code, headers,
history, encoding, reason, cookies, elapsed, request)

Wireshark:
5. Capture HTTP packets by visiting a HTTP Website, analyse the packets and
significance of its various fields. Do the same for HTTPS packets and compare
both


# CN_lab03

References:

● https://www.copernica.com/en/blog/post/a-record-and-mx-record-how-does-it-work

● https://www.utilizewindows.com/network-troubleshooting-using-ping-tracert-ipconfig-nslookup-commands/

● https://en.wikiversity.org/wiki/Wireshark/DNS


1. Develop a program to print the Mail exchange servers of a particular domain
with their preferences.

2. Use nslookup and ipconfig commands for finding various network related
information.

3. Capture and Analyse DNS Packets using Wireshark.
a. Analyse DNS Query and Response Packets.
b. By using the captured packets identify the source and destination ports
query and response messages.
c. Check whether a DNS request receives multiple responses, if so,
determine the reason for this

# CN_LAB04
References:
• https://pythonprogramming.net/python-port-scanner-sockets/

• https://en.wikiversity.org/wiki/Wireshark/UDP

1. Develop a basic port scanner to check if particular ports are open or closed for 
an input remote host.

2. Develop a threaded port scanner to check if particular ports are open or closed 
for a remote host. Determine which Port scanner is efficient.

3. Capture UDP packets and with the help of the captured UDP Packets.
a. analyse UDP DHCP Packets
b. analyse UDP DNS Packet

# CN_lab05

References:
• https://www.geeksforgeeks.org/secure-socket-layer-ssl/

• https://docs.python.org/3/library/ssl.html

• https://en.wikiversity.org/wiki/Wireshark/TCP

• https://www.youtube.com/watch?v=U9i7rWV-Gxo

1. Develop a code to illustrate a secure socket connection between client and 
server.
2. Capture TCP Packets and:
a. Analyse the three-way handshake during the establishment of the 
communication.
b. Identify if there are any retransmitted segments

