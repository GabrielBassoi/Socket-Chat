import socket
import select
import sys
from _thread import *
from xmlrpc.client import Server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP_address = "10.99.2.180" # input("Ip address: ")
Port = 5000 # int(input("Port: "))

server.bind((IP_address, Port))
server.listen(20)

lis = []


def clientthread(conn, addr):
    conn.send(b"Welcome to this chatroom!")

    while True:
        message = conn.recv(1024)
        if message:
            message_to_send = f"{message.decode('utf-8')}" # <{addr[0]}>
            print(message_to_send)
            message_to_send.encode("utf-8")
            # broadcast(message_to_send, conn)
            for c in lis:
                if c != conn:
                    c.send(message_to_send)


while True:
    conn, addr = server.accept()
    lis.append(conn)
    print(addr[0] + " connected")
    start_new_thread(clientthread, (conn, addr))

conn.close()
server.close()
