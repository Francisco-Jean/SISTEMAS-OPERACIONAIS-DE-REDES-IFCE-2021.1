from socket import *
import threading
from classes import *
from datetime import *
from time import *
from pickle import *
from threading import *
from cripto import *
from ast import literal_eval
from tkinter import *


# CRIANDO O SERVIDOR
server = socket(AF_INET, SOCK_STREAM)
host = gethostname()
porta = 20000
server.bind((host,porta))
server.listen()

# DESERIALIZANDO OS CLIENTES
with open('clientes.pickle', 'rb') as f:
    clientes = load(f)

# FUNÇÃO PRINCIPAL
def realiza_trabalho(client, addr):
    while 1:
        try: 
            verifica = client.recv(1024).decode('utf-8')
        except:
            client.close()
            print('O cliente se desconectou!')
            break

        # ENTRADA
        if verifica == '1':
            a = 1
            ver_conta = str(client.recv(1024).decode('utf-8'))
            ver_senha = str(client.recv(1024).decode('utf-8'))
            for x in clientes:
                if x.getConta() == ver_conta and x.getSenha() == ver_senha:
                    client.send('ok'.encode('utf-8'))
                    sleep(0.001)
                    client.send(x.getNome().encode('utf-8'))
                    sleep(0.001)
                    client.send(str(x.getSaldo()).encode('utf-8'))
                    sleep(0.001)
                    client.send(x.getEmail().encode('utf-8'))
                    sleep(0.001)
                    client.send(x.getCpf().encode('utf-8'))
                    print('Requisição do cliente concluida.\n\n-------------------------------------------')
                    break
                elif a == tamanho:
                    print(f'Ops! Cliente {ver_conta} não encontrado.\n\n-------------------------------------------')
                    client.send('n'.encode('utf-8'))
                a += 1

        # CADASTRO
        elif verifica == '2':
            b = 0
            recv_cpf = client.recv(1024).decode('utf-8')
            for y in clientes:
                if y.getCpf() == recv_cpf:
                    client.send('n'.encode('utf-8'))
                    print('O cliente tentou cadastrar um CPF já cadastrado.\n\n-------------------------------------------')
                    break
            else:
                client.send('ok'.encode('utf-8'))
                recv_nome = client.recv(1024).decode('utf-8')
                recv_email = client.recv(1024).decode('utf-8')
                recv_senha = client.recv(1024).decode('utf-8')
                clientes.append(cliente(recv_nome, recv_cpf, recv_email, recv_senha))
                with open('clientes.pickle', 'wb') as f:
                    dump(clientes, f)
                client.send(clientes[b-1].getConta().encode('utf-8'))
                print(f'Oba! O cliente {clientes[b-1].getConta()} foi cadastrado\n\n-------------------------------------------')
            b += 1

        # DEPÓSITO
        elif verifica == '3':
            ver_senha = client.recv(1024).decode('utf-8')
            for c in clientes:
                if c.getSenha() == ver_senha:
                    valor_deposito = float(client.recv(1024).decode('utf-8'))
                    c.setSaldo(c.getSaldo() + valor_deposito)
                    with open('clientes.pickle', 'wb') as f:
                        dump(clientes, f)
                    print('Oba! Saldo de ' + c.getNome() + ' Atualizado para ' + 
                    str(c.getSaldo()) + '\n\n-------------------------------------------')
                    break

        # SAQUE
        elif verifica == '4':
            ver_senha = client.recv(1024).decode('utf-8')
            for n in clientes:
                if n.getSenha() == ver_senha:
                    valor_saque = float(client.recv(1024).decode('utf-8'))
                    n.setSaldo(n.getSaldo() - valor_saque)
                    with open('clientes.pickle', 'wb') as f:
                        dump(clientes, f)
                    print('Oba! O Cliente Sacou R$ ' + str(valor_saque) + 
                    '\n\n-------------------------------------------')
                    break
        
        # TRANSFERÊNCIA
        elif verifica == '5':
            dados = client.recv(1024).decode('utf-8')
            dados = literal_eval(descriptografar(dados))
            for x in clientes:
                if x.getConta() == dados['conta']:
                    x.setSaldo(x.getSaldo() + float(dados['valor']))
                    for y in clientes:
                        if y.getConta() == dados['conta2']:
                            y.setSaldo(y.getSaldo() - float(dados['valor']))
                            client.send('ok'.encode('utf-8'))
                            break
                    with open('clientes.pickle', 'wb') as f:
                        dump(clientes, f)
                elif clientes.index(x) == (len(clientes) - 1):
                    client.send('n'.encode('utf-8'))
      
def mostrar():
    def line():
        return('\n' + ('---------------------------------------' * 2) + '\n')

    lista = Tk()
    lista.title('Clientes cadastrados')
    peoples = Text(lista)
    peoples.insert(END, '|{:<50s}|{:<10s}|{:<14s}|'.format('Nome', 'Conta', 'Senha') + line())
    for x in clientes:
        peoples.insert(END, '|{:<50s}|{:<10s}|{:<14s}|'.format(x.getNome(), x.getConta(), x.getSenha()) + line())
    peoples.pack(side = TOP)
    lista.mainloop()

l = Thread(target = mostrar)
l.start()

# INICIANDO A CONEXÃO            
while 1:
    tamanho = len(clientes)
    print('\nClientes cadastrados: ' + str(tamanho))
    print('Aguardando conexão do cliente...' )
    client, addr = server.accept()
    data = datetime.now()
    print(f'Oba! Cliente {addr} conectado as {data.hour} : {data.minute}')
    print('-------------------------------------------')
    t = Thread(target = realiza_trabalho, args = (client, addr))
    t.start()