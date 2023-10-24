import socket, sys, re, threading, json, sqlite3
from kafka import KafkaConsumer
from kafka import KafkaProducer
from json import dumps
from json import loads
from pymongo import MongoClient
import random
import requests
#from Crypto.Cipher import AES
import hashlib

#CAMBIAR VALORES POR PARÁMETROS
IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
ACTIVE_CONNS = 0
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

def consumer():
    print('ENTRA')
    consumer = KafkaConsumer('Engine', bootstrap_servers='172.27.224.219:9092')
    print('FAIL')
    fallo = False
    while True:
        for msg in consumer:
            print(str(msg.value, 'utf-8'))



def REG_Socket(ADDR):  
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(ADDR)
        print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")

        connected = True
        if connected:
            while True:
                # Nos piden introducir un username
                msg = client.recv(SIZE).decode(FORMAT)
                print(f"[SERVER] {msg}")

                # Introducimos username
                msg = input("> ")
                client.send(msg.encode(FORMAT))

                #El registry valida o deniega el username
                msg = client.recv(SIZE).decode(FORMAT)
                print(f"[SERVER] {msg}")

                if msg != "This user does not exist":
                        # Nos piden introducir un password
                        msg = client.recv(SIZE).decode(FORMAT)
                        print(f"[SERVER] {msg}")

                        # Introducimos password
                        msg = input("> ")
                        client.send(msg.encode(FORMAT))

                        #El registry valida o deniega el password
                        msg = client.recv(SIZE).decode(FORMAT)
                        print(f"[SERVER] {msg}")
                        
                        break
    except Exception as ex:
        print(f"¡¡¡¡ERROR!!!! {ex}")
    finally:
        client.close()



def AUTH_Socket(ADDR): 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(ADDR)
        print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")

        connected = True
        if connected:
            # Nos piden introducir un username
            msg = client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] {msg}")

            # Introducimos username
            msg = input("> ")
            client.send(msg.encode(FORMAT))

            #El registry valida o deniega el username
            msg = client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] {msg}")

            tmp_user = msg

            if msg != "Incorrect username. Choose a different username":
                # Nos piden introducir un password
                msg = client.recv(SIZE).decode(FORMAT)
                print(f"[SERVER] {msg}")

                # Introducimos password
                msg = input("> ")
                client.send(msg.encode(FORMAT))

                #El registry valida o deniega el password
                msg = client.recv(SIZE).decode(FORMAT)
                print(f"[SERVER] {msg}") 

                tmp_passwd = msg
    except Exception as ex:
        print(f"¡¡¡¡ERROR!!!! {ex}")
        return {"user": "ERROR", "password": "ERROR"}
    finally:
        client.close()
        return {"user": tmp_user, "password": tmp_passwd}


        

    

        

        
def main() -> int:
    while True:
        print("Select an option:\n 1. Register.\n 2. Start!")
        option = input("> ")

        if option == 1:
            # Conexión contra registry
            if REG_Socket():
                print("[DRONE] User successfully registered.")
            break
        elif option == 2:
            # Autenticar contra el engine 
            user_token = AUTH_Socket()

            #¿QUE MAS HABRIA QUE HACER?
            break
        else:
            print("Select a valid option (1 or 2)")

    consumer()

    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit