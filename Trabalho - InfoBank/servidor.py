from socket import *
from classes import *
from time import *

server = socket(AF_INET, SOCK_STREAM)

host = gethostname()
porta = 10000
server.bind((host,porta))
server.listen()

clientes = []
clientes.append(cliente('Jean', 1234, 'jean@eu', 1234))
clientes.append(cliente('Geovane', 4321, 'geo@email', 4321))
print('conta: ' + str(clientes[0].getConta()))
print('conta: ' + str(clientes[1].getConta()))
tamanho = len(clientes)
print('Tamanho da lista: ' + str(tamanho))
while 1:
    client, addr = server.accept()
    print(f'Conectado ao servidor: {addr}')
    while 1:
        y = 0
        verifica = client.recv(1024).decode('utf-8')
        if verifica == '1':
            ver_conta = int(client.recv(1024).decode('utf-8'))
            ver_senha = int(client.recv(1024).decode('utf-8'))
            for x in clientes:
                y += 1
                teste = x.getConta() == ver_conta and x.getSenha() == ver_senha
                if teste:
                    client.send('ok'.encode('utf-8'))
                    sleep(0.01)
                    client.send(x.getNome().encode('utf-8'))
                    sleep(0.01)
                    client.send(str(x.getSaldo()).encode('utf-8'))
                    sleep(0.01)
                    client.send(x.getEmail().encode('utf-8'))
                    sleep(0.01)
                    client.send(str(x.getCpf()).encode('utf-8'))
                    break
                elif y == tamanho:
                    print(f'cliente {ver_conta} não encontrado.')
                    client.send('n'.encode('utf-8'))

