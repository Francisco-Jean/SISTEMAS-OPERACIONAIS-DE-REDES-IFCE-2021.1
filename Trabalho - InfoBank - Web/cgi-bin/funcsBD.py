import mysql.connector
from random import randint

def retornaUsuario(nome):
    con = mysql.connector.connect(host = 'localhost', database = 'db_infobank', user = 'root', password = 'jean6032')
    comando = '''SELECT CPF, NUMERO, SALDO, usuario.idUSUARIO
                 FROM db_infobank.conta, db_infobank.usuario 
                 WHERE usuario.idUSUARIO = conta.idUSUARIO and usuario.NOME = '{}';'''.format(nome)
    cursor = con.cursor()
    cursor.execute(comando)
    user = cursor.fetchone()
    cursor.close()
    con.close() 
    return user

def retornaSaldo(nome):
    con = mysql.connector.connect(host = 'localhost', database = 'db_infobank', user = 'root', password = 'jean6032')
    comando = '''SELECT conta.idCONTA, SALDO FROM db_infobank.conta, db_infobank.usuario WHERE conta.idUSUARIO = usuario.idUSUARIO and usuario.NOME = '{}';'''.format(nome)
    cursor = con.cursor()
    cursor.execute(comando)
    dados = cursor.fetchone()
    conta = dados[0]
    saldo = dados[1]
    cursor.close()
    con.close() 
    return conta, saldo

def alterarSaldo(valor, idConta):
    con = mysql.connector.connect(host = 'localhost', database = 'db_infobank', user = 'root', password = 'jean6032')
    comando = '''UPDATE conta SET SALDO = '{}' WHERE (idCONTA = '{}');'''.format(valor, idConta)
    cursor = con.cursor()
    cursor.execute(comando)
    con.commit()
    cursor.close()
    con.close() 

def criarUsuario(nome, senha, cpf):
    con = mysql.connector.connect(host = 'localhost', database = 'db_infobank', user = 'root', password = 'jean6032')
    comando = '''INSERT INTO usuario (NOME, SENHA, CPF) VALUES ('{}', '{}', '{}');'''.format(nome, senha, cpf)
    cursor = con.cursor()
    cursor.execute(comando)
    con.commit()
    cursor.close()
    con.close() 

def criarConta(nome):
    numero = str(randint(1,9) * 1000 + randint(0,9) * 100 + randint(0,9) * 10 + randint(0,9))
    con = mysql.connector.connect(host = 'localhost', database = 'db_infobank', user = 'root', password = 'jean6032')
    comando = '''SELECT idUSUARIO FROM usuario WHERE NOME = '{}';'''.format(nome)
    cursor = con.cursor()
    cursor.execute(comando)
    id = cursor.fetchone()[0]
    comando = '''INSERT INTO conta (idUSUARIO, NUMERO, SALDO) VALUES ('{}', '{}', '0');'''.format(id, numero)
    cursor.execute(comando)
    con.commit()
    cursor.close()
    con.close() 

