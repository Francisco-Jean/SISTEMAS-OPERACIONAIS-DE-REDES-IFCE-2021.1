from index import *
from gtts import gTTS
import funcsBD

form = cgi.FieldStorage()

nome = form.getvalue('name')
cpf = form.getvalue('cpf')
senha = form.getvalue('password')

if nome and cpf and senha:
    funcsBD.criarUsuario(nome, senha, cpf)
    funcsBD.criarConta(nome)
    user = funcsBD.retornaUsuario(nome)
    cpf = user[0]
    conta = user[1]
    saldo = user[2]
    print(abrirArquivo('navbar.html').format(nome, nome, nome))
    print(abrirArquivo('home.html').format(nome, cpf, conta, saldo))
    voz = gTTS('     ........Olá, {}. Seja bem vindo ao InfoBênqui.'.format(nome), lang="pt-br").save('bevenido.mp3')
    print('''<audio autoplay>
                <source src="../bevenido.mp3" type="audio/mpeg">
             </audio>''')

else:
 print(abrirArquivo('subs.html'))

