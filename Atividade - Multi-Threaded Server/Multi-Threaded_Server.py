from socket import *
import threading

def handle_client(clientsocket, addr):
    peso = clientsocket.recv(1024).decode('utf-8')
    altura = clientsocket.recv(1024).decode('utf-8')
    imc = float(peso) / pow(float(altura), 2)
    clientsocket.send(str(imc).encode('utf-8'))
    clientsocket.close()

server = socket(AF_INET, SOCK_STREAM)
host = 'localhost'
port = 20000
server.bind((host, port))
server.listen()

while True:
    print('Aguardando cliente...')
    clientsocket, addr = server.accept()
    t = threading.Thread(target=handle_client, args=(clientsocket, addr))
    t.start() 