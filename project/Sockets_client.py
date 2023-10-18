import socket
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
ACTIVE_CONNS = 0
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

def Sockets_client(): 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")

    connected = True
    while connected:
        msg = input("> ")
        client.send(msg.encode(FORMAT))

        if msg == DISCONNECT_MSG:
            connected = False
        else:
            msg = client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] {msg}")