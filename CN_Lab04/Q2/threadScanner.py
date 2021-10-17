# Develop a threaded port scanner to check if particular ports are open or closed
# for a remote host. Determine which Port scanner is efficient.
import threading
import socket
from queue import Queue

print_lock = threading.Lock()

target = input("Enter the Target")
low=int(input('Enter the lower_bound'))
high=int(input("Enter the higher_bound"))



def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        with print_lock:
            print(port, 'is open\n')
        con.close()
    except:
        pass


# The threader thread pulls an worker from the queue and processes it
def threader():
    while True:
        # gets an port from the queue
        port = q.get()

        #scan the port
        portscan(port)
        # mark complete after complition
        q.task_done()


# Create the queue and threader
q = Queue()
no_thread=int(input("Enter the number of thereads"))
# how many threads are we going to allow for
for x in range(no_thread):
    t = threading.Thread(target=threader)
    # classifying as a daemon, so they will die when the main dies
    t.daemon = True
    # begins, must come after daemon definition
    t.start()

for port in range(low, high):
    q.put(port)

# wait until the thread terminates.
q.join()
