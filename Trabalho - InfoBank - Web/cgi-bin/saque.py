import cgitb, cgi
from open import *
cgitb.enable()
import funcsBD
from gtts import gTTS

form = cgi.FieldStorage()
nome = form.getvalue('name')
valor = form.getvalue('valor')

if valor:
    print(type(valor))
    conta, saldo = funcsBD.retornaSaldo(nome)
    saldo -= float(valor)
    funcsBD.alterarSaldo(saldo, conta)
    print("Content-type:text/html\r\n\r\n")
    print(abrirArquivo('navbar.html').format(nome, nome, nome))
    voz = gTTS('     .....Saque no valor de {} reais realizado com sucesso.'.format(valor), lang="pt-br").save('saque.mp3')
    print('''<audio autoplay>
                <source src="../saque.mp3" type="audio/mpeg">
             </audio>''')

else:
    print("Content-type:text/html\r\n\r\n")
    print(abrirArquivo('navbar.html').format(nome, nome, nome))

print(abrirArquivo('saque.html').format(nome))