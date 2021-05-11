from tkinter import *
from tkinter import ttk
from socket import *
from time import *
from tkinter import messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

def converte(tamanho):
    return tamanho/0.352777

# DADOS DO CLIENTE ATUAL
clienteAtual = {'nome' : 'default', 'conta' : '0', 'saldo' : 1000.0, 'email' : 'default',
'cpf' : 'default', 'senha' : '0'}

# CONECTANDO AO SERVIDOR
host = gethostname()
porta = 20000

# CONFIGURAÇÕES PADRÃO
cor_p = '#91b0b3'
fonte_p = 'Cooper Black'

# FUNÇÃO DO BOTÃO PARA VOLTAR A TELA INICIAL
def voltar_inicio():
    j.title('InfoBank - O Banco Mais Tech do Brasil')
    fc.forget()
    fe.forget()
    f1.pack(side = TOP)
    erro_e.configure(text = '')

# JANELA DE CADASTRO - TKINTER
def cadastro():
    f1.forget()
    fc.pack(side = TOP)
    j.title('InfoBank - Cadastro')

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

    erro_c.pack(side = TOP, pady = (20,0))

    salvar_dados.pack(side = TOP, pady = (25,2))

    Button(fc, text = 'VOLTAR',width = 8, height = 1, bd = 5, font = (fonte_p, 10, 'bold'),
    fg = '#ffffff', bg = '#6f9596', relief = RIDGE, command = voltar_inicio).pack(side = TOP, 
    padx = (10,380), pady = 25)

# JANELA DE LOGIN - TKINTER
def entrar():
    j.title('InfoBank - Login')
    f1.forget()
    fe.pack(side = TOP, anchor = 'n')

    Label(fe, text = 'ENTRE', font = (fonte_p, '20', 'bold'), bg = cor_p, 
    fg = 'white').pack(side = TOP)

    Label(fe, text = 'CONTA', font = (fonte_p, '15', 'bold'), bg = cor_p, 
    fg = 'white').pack(side = TOP, padx = 5, pady = (20,0))

    conta_e.pack(side = TOP)

    Label(fe, text = 'SENHA:', font = (fonte_p, '15', 'bold'), bg = cor_p, 
    fg = 'white').pack(side = TOP, padx = 5, pady = (20,0))

    senha_e.pack(side = TOP)

    erro_e.pack(side = TOP, pady = (20,0))

    entrar_d.pack(side = TOP, pady = (41,21), anchor = S)

    Button(fe, text = 'VOLTAR',width = 8, height = 1, bd = 5, font = (fonte_p, 10, 'bold'),
    fg = '#ffffff', bg = '#6f9596', relief = RIDGE, command = voltar_inicio).pack(side = TOP, 
    padx = (10,380), pady = (66,101))

# FUNÇÃO DO LOGIN
def logar():
    if conta_e.get() == '' or senha_e.get() == '':
        erro_e.configure(text = 'Informe todos os dados!')
    else:
        server = socket(AF_INET, SOCK_STREAM)
        server.connect((host,porta))
        clienteAtual['conta'] = str(conta_e.get())
        server.send('1'.encode('utf-8'))
        sleep(0.001)
        server.send(clienteAtual['conta'].encode('utf-8'))
        sleep(0.001)
        server.send(senha_e.get().encode('utf-8'))
        autoriza = server.recv(1024).decode('utf-8')
        if autoriza == 'ok':
            clienteAtual['nome'] = server.recv(1024).decode('utf-8')
            clienteAtual['saldo'] = float(server.recv(1024).decode('utf-8'))
            clienteAtual['email'] = server.recv(1024).decode('utf-8')
            clienteAtual['cpf'] = server.recv(1024).decode('utf-8')
            clienteAtual['senha'] = str(senha_e.get())
            Home()
            server.close()
        elif autoriza == 'n':
            erro_e.configure(text = 'Ops! Dados inválidos. Tente novamente...')
        else:
            erro_e.configure(text = 'Ops! Um erro inesperado ocorreu. Por favor, tente novamente.')

# FUNÇÃO DO CADASTRO
def cadastrar():
    if nome_c.get() == '' or cpf_c.get() == '' or email_c.get() == '' or senha_c.get() == '':
        erro_c.configure(text = 'Preencha todos os campos!')
    else:
        server = socket(AF_INET, SOCK_STREAM)
        server.connect((host,porta))
        server.send('2'.encode('utf-8'))
        sleep(0.001)
        server.send(cpf_c.get().encode('utf-8'))
        visto = server.recv(1024).decode('utf-8')
        if visto == 'n':
            erro_c.configure(text = 'Ops! CPF já cadastrado.')
        elif visto == 'ok':
            sleep(0.001)
            server.send(nome_c.get().encode('utf-8'))
            sleep(0.001)
            server.send(email_c.get().encode('utf-8'))
            sleep(0.001)
            server.send(senha_c.get().encode('utf-8'))
            clienteAtual['conta'] = server.recv(1024).decode('utf-8')
            clienteAtual['nome'] = nome_c.get()
            clienteAtual['email'] = email_c.get()
            clienteAtual['cpf'] = cpf_c.get()
            clienteAtual['senha'] = str(senha_c.get())
            server.close()
            Home()
            messagebox.showinfo('InfoBank : Bem - Vindo!', message = "Olá, seja muito bem vindo ao InfoBank, o maior e melhor banco virtual do Brasil! Para comemorar sua chegada, acabados de depositar R$ 1.000 na sua conta. Aproveite!")
        else:
            erro_c.configure(text = 'Ops! Um erro inesperado ocorreu. Por favor, tente novamente.')

# FUNÇÃO PARA REALIZAR UM DEPÓSITO
def realizarDeposito():
    if valor_deposito.get() == '' or senha_deposito.get() == '':
        erro_deposito.configure(text = 'Informe todos os dados!')
    elif senha_deposito.get() != clienteAtual['senha']:
        erro_deposito.configure(text = 'Ops! Senha incorreta. Tente novamente...')
    else:
        server = socket(AF_INET, SOCK_STREAM)
        server.connect((host,porta))
        server.send('3'.encode('utf-8'))
        sleep(0.001)
        server.send(senha_deposito.get().encode('utf-8'))
        sleep(0.001)
        server.send(valor_deposito.get().encode('utf-8'))
        clienteAtual['saldo'] += float(valor_deposito.get())
        conta_dados.configure(text = clienteAtual['conta'] +
        '\n\n\nR$ ' + str(clienteAtual['saldo']))
        messagebox.showinfo('Depósito Concluído', message = 'Oba! Depósito no valor de R$ ' +
        valor_deposito.get() + ' realizado com sucesso!')
        server.close()

# FUNÇÃO PARA REALIZAR UM SAQUE
def realizarSaque():
    if valor_saque.get() == '' or senha_saque.get() == '':
        erro_saque.configure(text = 'Informe todos os dados!')
    elif senha_saque.get() != clienteAtual['senha']:
        erro_saque.configure(text = 'Ops! Senha incorreta. Tente novamente...')
    else:
        server = socket(AF_INET, SOCK_STREAM)
        server.connect((host,porta))
        server.send('4'.encode('utf-8'))
        sleep(0.001)
        server.send(senha_saque.get().encode('utf-8'))
        sleep(0.001)
        server.send(valor_saque.get().encode('utf-8'))
        clienteAtual['saldo'] -= float(valor_saque.get())
        conta_dados.configure(text = clienteAtual['conta'] +
        '\n\n\nR$ ' + str(clienteAtual['saldo']))
        messagebox.showinfo('Saque Concluído', message = 'Oba! Saque no Valor de R$ ' +
        valor_saque.get() + ' realizado com sucesso!')
        server.close()

# FUNÇÃO PARA GERAR O EXTRATO
def gerarExtrato():
    
    linha = '-----------------------------------------------------------------------'
    arquivo = canvas.Canvas('C:/Users/jeans/Downloads' + '\\extrato.pdf',
    pagesize = A4)
    arquivo.drawString(converte(50),converte(290),'EXTRATO')
    arquivo.drawString(converte(10),converte(280),linha)
    texto1 = 'NOME:     ' + clienteAtual['nome']
    texto2 = 'CONTA:   ' + clienteAtual['conta']
    texto3 = 'SALDO:   R$ ' + str(clienteAtual['saldo'])
    arquivo.drawString(converte(10),converte(260),texto1)
    arquivo.drawString(converte(10),converte(250),texto2)
    arquivo.drawString(converte(10),converte(240),texto3)
    arquivo.drawString(converte(10),converte(220),linha)
    arquivo.save()

# JANELA HOME - TKINTER
def Home():
    j.title('InfoBank - HOME')
    fc.forget()
    fe.forget()
    img_label.forget()
    j.geometry('1350x700+2+10')
    opc.add(dados_conta, text = 'Dados da Conta')
    opc.add(dados_cliente, text = 'Meus Dados')
    opc.add(cliente_deposito, text = 'Deposito')
    opc.add(cliente_saque, text = 'Sacar')
    opc.add(cliente_extrato, text = 'Extrato')

    opc.place(x = 0, y = 0, width = 1366, height = 768)

    Label(dados_conta, text = '💰', bg = cor_p, fg = '#7c9da1',
    font = ('', 300)).place(x = 900, y = 230)

    Label(dados_conta, text = '➤ CONTA:\n\n\n➤ SALDO:', justify = LEFT, bg = cor_p, fg = 'white', 
    font = (fonte_p, 30, 'bold')).place(x = 60, y = 230)

    conta_dados.configure(text = clienteAtual['conta'] + 
    '\n\n\nR$ ' + str(clienteAtual['saldo']))

    conta_dados.place(x = 310, y = 230)

    Label(dados_cliente, text = '👨‍💻', bg = cor_p, fg = '#7c9da1',
    font = ('', 300)).place(x = 900, y = 230)

    Label(dados_cliente, text = '✑ NOME:\n\n\n✑ CPF:\n\n\n✑ EMAIL:', justify = LEFT, bg = cor_p, fg = 'white', 
    font = (fonte_p, 30, 'bold')).place(x = 60, y = 150)

    cliente_dados = Label(dados_cliente, bg = cor_p, font = (fonte_p, 30), justify = LEFT,
    text = clienteAtual['nome'] + '\n\n\n' + clienteAtual['cpf'] + '\n\n\n' + clienteAtual['email'])
    cliente_dados.place(x = 310, y = 150)

    # JANELA DE DEPÓSITO
    Label(cliente_deposito, text = '💵', bg = cor_p, fg = '#7c9da1',
    font = ('', 220)).place(x = 20, y = 350)

    Label(cliente_deposito, text = 'Olá, ' + clienteAtual['nome'] + '.\nQuanto você quer depositar?',
    bg = cor_p, fg = 'white', font = (fonte_p, 35, 'bold')).pack(side = TOP, pady = (100, 20))

    Label(cliente_deposito, text = 'VALOR:', font = (fonte_p, 20), bg = cor_p, 
    fg = 'white').pack(side = TOP, pady = (40, 10))

    valor_deposito.pack(side = TOP, pady = (0, 40))

    Label(cliente_deposito, text = 'SENHA:', font = (fonte_p, 20), bg = cor_p, 
    fg = 'white').pack(side = TOP, pady = (20, 10))

    senha_deposito.pack(side = TOP, pady = (0, 40))

    erro_deposito.pack(side = TOP, pady = 10)

    bt_deposito.pack(side = TOP, pady = 20)

    # JANELA DE SAQUE
    Label(cliente_saque, text = '💸', bg = cor_p, fg = '#7c9da1',
    font = ('', 220)).place(x = 1000, y = 320)

    Label(cliente_saque, text = 'Olá, ' + clienteAtual['nome'] + '.\nQuanto você quer sacar?',
    bg = cor_p, fg = 'white', font = (fonte_p, 35, 'bold')).pack(side = TOP, pady = (100, 20))

    Label(cliente_saque, text = 'VALOR:', font = (fonte_p, 20), bg = cor_p, 
    fg = 'white').pack(side = TOP, pady = (40, 10))

    valor_saque.pack(side = TOP, pady = (0, 40))

    Label(cliente_saque, text = 'SENHA:', font = (fonte_p, 20), bg = cor_p, 
    fg = 'white').pack(side = TOP, pady = (20, 10))

    senha_saque.pack(side = TOP, pady = (0, 40))

    erro_saque.pack(side = TOP, pady = 10)

    bt_saque.pack(side = TOP, pady = 20)

    # JANELA DE EXTRATO
    Label(cliente_extrato, text = '📄', bg = cor_p, fg = '#7c9da1',
    font = ('', 220)).place(x = 1000, y = 320)

    Label(cliente_extrato, text = 'Olá, ' + clienteAtual['nome'] + '.\nPara gerar seu extrato, clique aqui:',
    bg = cor_p, fg = 'white', font = (fonte_p, 35, 'bold')).pack(side = TOP, pady = (150, 20))

    bt_extrato.pack(side = TOP, pady = 50)

# JANELA INICIAL
j = Tk()
j.geometry('530x738+750+0')
j['bg'] = cor_p
j.title('InfoBank - O Banco Mais Tech do Brasil')
img = PhotoImage(file='Logo.gif')
img_label = Label(j, image = img, bg = cor_p)
img_label.pack(side = TOP)

barra = Frame(j, height = 3)

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
erro_c = Label(fc, text = ' ', bg = cor_p, fg = 'red', font = ('', 13))
salvar_dados = Button(fc, text = 'CADASTRAR', bd = '5', font = (fonte_p, 15, 'bold'),
fg = '#ffffff', bg = '#6f9596', width = 12, relief = RIDGE, command = cadastrar)

# JANELA DE LOGIN
fe = Frame(j, bg = cor_p)
conta_e = Entry(fe, width = 35)
senha_e = Entry(fe, width = 35, show = '*')
erro_e = Label(fe, text = ' ', bg = cor_p, fg = 'red', font = ('', 13))
entrar_d = Button(fe, text = 'ENTRAR', bd = '5', font = (fonte_p, 15, 'bold'),
fg = '#ffffff', bg = '#6f9596', width = 12, relief = RIDGE, command = logar)

# JANELA - HOME
opc = ttk.Notebook(j)
dados_cliente = Frame(opc, bg = cor_p)
dados_conta = Frame(opc, bg = cor_p)
cliente_deposito = Frame(opc, bg = cor_p)
cliente_saque = Frame(opc, bg = cor_p)
cliente_extrato = Frame(opc, bg = cor_p)

conta_dados = Label(dados_conta, bg = cor_p, font = (fonte_p, 30), justify = LEFT,
text = clienteAtual['conta'] + '\n\n\nR$ ' + str(clienteAtual['saldo']))

valor_deposito = Entry(cliente_deposito, width = 30)
senha_deposito = Entry(cliente_deposito, width = 30)
erro_deposito = Label(cliente_deposito, text = '', font = (fonte_p, 15), bg = cor_p, fg = 'red')
bt_deposito = Button(cliente_deposito, text = 'DEPOSITAR', bd = '5', font = (fonte_p, 30, 'bold'),
fg = '#ffffff', bg = '#6f9596', width = 12, relief = RIDGE, command = realizarDeposito)

valor_saque = Entry(cliente_saque, width = 30)
senha_saque = Entry(cliente_saque, width = 30)
erro_saque = Label(cliente_saque, text = '', font = (fonte_p, 15), bg = cor_p, fg = 'red')
bt_saque = Button(cliente_saque, text = 'SACAR', bd = '5', font = (fonte_p, 30, 'bold'),
fg = '#ffffff', bg = '#6f9596', width = 12, relief = RIDGE, command = realizarSaque)

bt_extrato = Button(cliente_extrato, text = 'GERAR EXTRATO', bd = '5', font = (fonte_p, 30, 'bold'),
fg = '#ffffff', bg = '#6f9596', relief = RIDGE, command = gerarExtrato)

j.mainloop()
