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

list_of_clients = []


def clientthread(conn, addr):
    conn.send(b"Welcome to this chatroom!")

    while True:
        try:
            message = conn.recv(1024)
            if message:
                message_to_send = f"<{addr[0]}>{message.decode('utf-8')}"
                print(message_to_send)
                message_to_send = message_to_send.encode("utf-8")
                broadcast(message_to_send, conn)
            else:
                remove(conn)
        except:
            continue


def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message)
            except:
                clients.close()
                remove(clients)


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print(addr[0] + " connected")
    start_new_thread(clientthread, (conn, addr))

conn.close()
server.close()
