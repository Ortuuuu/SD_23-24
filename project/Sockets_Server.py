import socket
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
ACTIVE_CONNS = 0
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

def handle_client(conn, addr): 

    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg = conn.recv(SIZE).decode(FORMAT)

        if msg == DISCONNECT_MSG:
            connected = False
            print(f"[NEW DISCONNECTION] {addr} disconnected.")
        else:
            print(f"[{addr}] {msg}")
            # TRABAJAR CON EL MENSAJE RECIBIDO, AQUI SOLO SE MUESTRA POR CONSOLA A MODO DE EJEMPLO
    
    conn.close()


def socketServer():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        ACTIVE_CONNS = threading.active_count() - 1
        
