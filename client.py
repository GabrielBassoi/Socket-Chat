import socket
import sys
from threading import Thread
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IP_address = "192.168.1.184" # input("IP address: ")
Port = 5000 # int(input("Port: "))
Name = "Gabriel" # input("Name: ")

server.connect((IP_address, Port))

def listen_messages():
    while True:
        message = server.recv(1024)
        if message != None:
            print(message.decode("utf-8"))

thread = Thread(target=listen_messages)
thread.daemon = True
thread.start()

while True:
    text = input()
    message = f"<{Name}> " + text
    messageb = message.encode("utf-8")
    server.send(messageb)
    
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')
    sys.stdout.write("<You> ")
    sys.stdout.write(text + "\n")
    sys.stdout.flush()



# while True:
#     sockets_list = [sys.stdin, server]
#     read_sockets, write_socket, error_socket = select.select(sockets_list,[],[])
#     for socks in read_sockets:
#         if socks == server:
#             message = socks.recv(2048)
#             message = message.decode('utf-8')
#             print(message)
#         else:
#             message = sys.stdin.readline()
#             messageb = message.encode("utf-8")
#             server.send(messageb)
#             sys.stdout.write("<You>")
#             sys.stdout.write(message)
#             sys.stdout.flush()
# server.close()
