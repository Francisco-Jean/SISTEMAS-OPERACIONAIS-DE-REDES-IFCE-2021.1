from tkinter import *
from socket import *
from time import *

# DADOS DO CLIENTE ATUAL
clienteAtual = {'nome' : '', 'conta' : '', 'saldo' : 0, 'email' : ''}

# CONECTANDO AO SERVIDOR
server = socket(AF_INET, SOCK_STREAM)
'''host = gethostname()
porta = 10000

server.connect((host,porta))'''

# CONFIGURAÇÕES PADRÃO
cor_p = '#91b0b3'
fonte_p = 'Gill Sans Ultra Bold'

# FUNÇÃO DO BOTÃO PARA VOLTAR A TELA INICIAL
def voltar_inicio():
    j.title('InfoBank - O Banco Mais Tech do Brasil')
    fc.forget()
    fe.forget()
    f1.pack(side = TOP)

# JANELA DE CADASTRO - FUNÇÃO
def cadastro():
    f1.forget()
    fc.pack(side = TOP)

    Label(fc, text = 'CADASTRE-SE', font = (fonte_p, '20', 'bold'), bg = cor_p, 
    fg = 'white').pack(side = TOP, pady = (3,0))

    Label(fc, text = 'Nome:', font = (fonte_p, '15', 'bold'), bg = cor_p, 
    fg = 'white').pack(side = TOP, pady = (15,0))

    nome_c.pack(side = TOP)

    Label(fc, text = 'CPF:', font = (fonte_p, '15', 'bold'), bg = cor_p, 
    fg = 'white').pack(side = TOP, pady = (25,0))

    cpf_c.pack(side = TOP)

    Label(fc, text = 'EMAIL:', font = (fonte_p, '15', 'bold'), bg = cor_p, 
    fg = 'white').pack(side = TOP, pady = (25,0))

    email_c.pack(side = TOP)

    Label(fc, text = 'SENHA:', font = (fonte_p, '15', 'bold'), bg = cor_p, 
    fg = 'white').pack(side = TOP, pady = (25,0))

    senha_c.pack(side = TOP)

    salvar_dados.pack(side = TOP, pady = (25,0))

    Button(fc, text = 'VOLTAR', bd = 5, font = (fonte_p, 10, 'bold'),
    fg = '#ffffff', bg = '#6f9596', relief = RIDGE, command = voltar_inicio).pack(side = TOP, 
    padx = (0,400), pady = 22)


# JANELA DE LOGIN - FUNÇÃO
def entrar():
    j.title('InfoBank - Login')
    f1.forget()
    fe.pack(side = TOP, anchor = 'n')

    Label(fe, text = 'ENTRE', font = (fonte_p, '20', 'bold'), bg = cor_p, 
    fg = 'white').pack(side = TOP, padx = (0,0))

    Label(fe, text = 'CONTA', font = (fonte_p, '15', 'bold'), bg = cor_p, 
    fg = 'white').pack(side = TOP, padx = 5, pady = (20,0))

    conta_e.pack(side = TOP)

    Label(fe, text = 'SENHA:', font = (fonte_p, '15', 'bold'), bg = cor_p, 
    fg = 'white').pack(side = TOP, padx = 5, pady = (20,0))

    senha_e.pack(side = TOP)

    entrar_d.pack(side = TOP, pady = (50,20), anchor = S)

    Button(fe, text = 'VOLTAR', bd = 5, font = (fonte_p, 10, 'bold'),
    fg = '#ffffff', bg = '#6f9596', relief = RIDGE, command = voltar_inicio).pack(side = TOP, 
    padx = (0,400), pady = 82)

# VERIFICANDO OS DADOS
def logar():
    if conta_e.get() == '' or senha_e.get() == '':
        print('Tome vergonha, entre com um valor aí va lá.')
    else:
        clienteAtual['conta'] = conta_e.get()
        server.send('1'.encode('utf-8'))
        sleep(0.01)
        server.send(clienteAtual['conta'].encode('utf-8'))
        sleep(0.01)
        server.send(senha_e.get().encode('utf-8'))
        altoriza = server.recv(1024).decode('utf-8')
        if altoriza == 'ok':
            clienteAtual['nome'] = server.recv(1024).decode('utf-8')
            clienteAtual['saldo'] = int(server.recv(1024).decode('utf-8'))
            clienteAtual['email'] = server.recv(1024).decode('utf-8')
            clienteAtual['cpf'] = int(server.recv(1024).decode('utf-8'))
            print('Bem-vindo, ' + clienteAtual['nome'])
            print('Seu saldo : R$ ' + str(clienteAtual['saldo']))
            print('Email: ' + clienteAtual['email'])
            print('CPF: ' + str(clienteAtual['cpf']))
        elif altoriza == 'n':
            print('Ops! Os dados inseridos são inválidos. Tente novamente...')

# HOME - FUNÇÂO
def Home():
    fc.forget()
    fe.forget()
    f1.forget()
    img_label.forget()
    saldo_bt.place(x = 50, y = 50)


# JANELA INICIAL
j = Tk()
j.geometry("{0}x{1}+0+0".format(j.winfo_screenwidth(), j.winfo_screenheight()))
j['bg'] = cor_p
j.title('InfoBank - O Banco Mais Tech do Brasil')
img = PhotoImage(file='Logo_cortado.gif')
img_label = Label(j, image = img, bg = cor_p)
img_label.pack(side = TOP)

f1 = Frame(j, bg = cor_p)
f1.pack(side = TOP)

# BOTÃO DE CADASTRO
cadastro_bt = Button(f1, text = 'CADASTRAR', bd = '5', font = (fonte_p, 20, 'bold'),
fg = '#ffffff', bg = '#6f9596', width = 12, relief = RIDGE, command = cadastro)
cadastro_bt.pack(side = TOP, pady = (120,20))

# BOTÃO DE LOGIN
login_bt = Button(f1, text = 'ENTRAR', bd = '5', font = (fonte_p, 20, 'bold'),
fg = '#ffffff', bg = '#6f9596', width = 12, relief = RIDGE, command = entrar)
login_bt.pack(side = TOP, pady = 20)

# RODAPÉ
Label(j, text = 'Copyright © 2021 | Todos os direitos reservados - InfoBank', 
bg = 'White').pack(side = BOTTOM, fill = 'x')

# JANELA DE CADASTRO
fc = Frame(j, bg = cor_p)
j.title('InfoBank - Cadastro')
nome_c = Entry(fc, width = 35)
cpf_c = Entry(fc, width = 35)
email_c = Entry(fc, width = 35)
senha_c = Entry(fc, width = 35, show = '*')
salvar_dados = Button(fc, text = 'CADASTRAR', bd = '5', font = (fonte_p, 15, 'bold'),
fg = '#ffffff', bg = '#6f9596', width = 12, relief = RIDGE, command = 1)

# JANELA DE LOGIN
fe = Frame(j, bg = cor_p)
conta_e = Entry(fe, width = 35)
senha_e = Entry(fe, width = 35, show = '*')
entrar_d = Button(fe, text = 'ENTRAR', bd = '5', font = (fonte_p, 15, 'bold'),
fg = '#ffffff', bg = '#6f9596', width = 12, relief = RIDGE, command = logar)

# JANELA - HOME
home = Frame(j)
saldo_bt = Button(home, text = 'SALDO', bd = '10', font = (fonte_p, 15, 'bold'),
fg = '#ffffff', bg = '#6f9596', relief = RIDGE, command = 1)

j.mainloop()


