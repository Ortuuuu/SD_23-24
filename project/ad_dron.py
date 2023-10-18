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


def consumer():
    print('ENTRA')
    consumer = KafkaConsumer('Engine', bootstrap_servers='172.27.224.219:9092')
    print('FAIL')
    fallo = False
    while True:
        for msg in consumer:
            print(str(msg.value, 'utf-8'))
        
        
def main() -> int:
    consumer()
    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit




