from socket import *
from time import sleep
host = 'localhost'
port = 20000
while 1:
    try:
        x = int(input('------------------------\nO que queres fazer agora?\nDigite 1 para calcular o IMC.\nDigite 2 Para SAIR.\n\nOPÇÃO:'))
        if x == 1:
            server = socket(AF_INET, SOCK_STREAM)
            peso = float(input('Digite o seu peso: '))
            altura = float(input('Digite a sua altura: '))
            server.connect((host, port))
            server.send(str(peso).encode('utf-8'))
            sleep(0.001)
            server.send(str(altura).encode('utf-8'))
            c = server.recv(1024).decode('utf-8')
            print("\033[0;32m" + '\nSeu IMC é: %.2f' % float(c) + "\033[0;0m")
            server.close()
        elif x == 2:
            print('\nFinalizando...')
            break
        else:
            print("\033[1;31m" + '\nOpção inválida. Tente novamente.\n' + "\033[0;0m")
    except:
        print("\033[1;31m" + '\nValor inválido. Tente novamente.\n' + "\033[0;0m")
    