from socket import *

server = socket(AF_INET, SOCK_STREAM)

host = gethostname()
porta = 1010
server.bind((host,porta))
server.listen()

while 1:
    client, addr = server.accept()
    print('Conectado ao servidor: ' + addr)