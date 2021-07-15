#!/usr/bin/python
import cgitb, cgi
from open import *
cgitb.enable()
import funcsBD

form = cgi.FieldStorage()
nome = form.getvalue('name')

print("Content-type:text/html\r\n\r\n")
print(abrirArquivo('navbar.html').format(nome, nome, nome))

if __name__ == '__main__':
    user = funcsBD.retornaUsuario(nome)

    cpf = user[0]
    conta = user[1]
    saldo = user[2]
    print(abrirArquivo('home.html').format(nome, cpf, conta, saldo))