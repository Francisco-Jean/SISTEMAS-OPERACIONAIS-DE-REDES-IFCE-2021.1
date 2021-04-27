from tkinter import *

j = Tk()
j.title('Conversor de medidas')
j.geometry('600x640')

f1 = Frame(j, borderwidth = 2, relief = 'solid', bg = '#dcdcdc')
f1.place(x = 10 , y = 10, width = 580, height = 300)
l1 = Label(f1, text = 'TEMPO', font = ('Constantia', '15', 'bold'), bg = '#dcdcdc')
l1.place(x = 5, y = 5)
Label(f1, text = 'DE:', bg = '#dcdcdc', font = ('Constantia', '10', 'bold')).place(x = 10, y = 40)
bs1 = Button(f1, text = "SALVAR", bg = '#000', fg = '#fff')
bs1.place(x = 240, y = 250, width = 100)

j.mainloop()