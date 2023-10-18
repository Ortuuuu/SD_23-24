#import socket, sys, re, threading, kafka, json, sqlite3
#from time import sleep
from kafka import KafkaConsumer
from kafka import KafkaProducer
import sys
#from json import dumps
#import random
#import requests
#from Crypto.Cipher import AES
#import hashlib

FORMAT = 'utf-8'
FIN = "FIN"    
HEADER = 64
#try:
    #IP_BROKER = sys.argv[1]
    #PUERTO_BROKER = int(sys.argv[2])
    #MAX_VISITANTES = int(sys.argv[3])
    #IP_WAITING_SERVER = sys.argv[4]
    #PUERTO_WAITING_SERVER = int(sys.argv[5])
#except IndexError:
#    print("ERROR")
#    print(bcolors.FAIL +'FWQ_Engine requiere <IP_BROKER> <PUERTO_BROKER> <MAX_VISITANTES> <IP_FWQ_WAITINGTIMESERVER> <PUERTO_FWQ_WAITINGTIMESERVER>' + bcolors.RESET)

#except ValueError:
#    print("ERROR")
#    print(bcolors.FAIL + 'No se puede convertir una palabra a un int. Por favor, introduce los datos correctamente.' + bcolors.RESET)
        

def producirKafka(data):
    #connection = sqlite3.connect('user.db')
    #c = connection.cursor()
    #c.execute("select * from user where inPark = 1")
    #usuariosEnMapa = c.fetchall() #MAS ADELANTE NECESITAREMOS PASARLE LOS USUARIOS TAMBIEN.
    
        #Creamos un productor para enviar solo un mensaje.
        #producer = KafkaProducer(bootstrap_servers=IP_BROKER+':'+ str(PUERTO_BROKER),
        #                    value_serializer=lambda x:dumps(x).encode('utf-8'))
        
        producer = KafkaProducer(bootstrap_servers='172.27.224.219:9092')
        producer.send('Engine', value = bytes (data, 'utf-8'))
        print('SIN ERRORES')

        #print(bcolors.FAIL +'Actualmente no hay un broker disponible en la dirección ' + IP_BROKER +':'+PUERTO_BROKER + '. Espere a que se inicie el broker si la direccion es correcta o vuelva a intentarlo con otra dirección.' + bcolors.RESET)




def main() -> int:
    contDrones = 0
    data = 'hola'
    fich = input('Fichero para la figura: ')
    fichero = open(fich, 'r')
    lineas = fichero.readline()
    for line in lineas:
        line.strip()
        datos = line.split(' ')
        data = 'Dron id: ' + datos[0] + ', va a las coordenadas X: ' + datos[0] + ' e Y: ' + datos[0]
        print(data)
        s = bytes(data, 'utf-8')
        #producirKafka(datos)

    fichero.close()
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit