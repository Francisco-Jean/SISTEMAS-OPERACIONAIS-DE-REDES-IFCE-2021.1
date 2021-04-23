from tkinter import *
from random import *

def sorteio():
    n = sample(range(1,61), 6)
    z = f'\nNÚMEROS SORTEADOS:\n{n[0]}, {n[1]}, {n[2]}, {n[3]}, {n[4]} e {n[5]}'
    x.configure(text=z)
    
janela = Tk()
janela.title('Sorteador')
janela.geometry('305x200')
x = Label(janela, text='', fg = 'red')
x.grid(column=0, row=1)
bot = Button(janela, text='SORTEAR',command=sorteio)
bot.grid(column=0,row=0)
l = Label(janela, text='\n\n\nO sorteador irá mostrar 6 \
números aleatórios entre 1 e 60\nEscolha os seus números! \n\nBOA SORTE!')
l.grid(column=0,row=3)

janela.mainloop()
