line = '.-------------------'

def l():
    print(f'{line * 6}.')

def wr(li):
    for x in li:
        print('|{:19s}'.format(x), end="")
    print('|')
    l()

l()
print("| Lista de Produtos |    QTD Entradas   |     QTD Saídas    |   Saldo Estoque   |   Preço Unitário  |     Subtotal      |")
l()

wr(['Azeite de Oliva', '100', '40', '60', '21,90', '1.314,00'])
wr(['Castanha do Pará', '100', '5', '95', '6,00', '300,00'])
wr(['Flocos de Aveia', '1000', '200', '800', '10,90', '872,00'])
wr(['Paçoca de Amendoim', '100', '8', '92', '1,50', '30,00'])
wr(['Panetone s/ Gluten', '100', '60', '40', '17,30', '692,00'])
wr(['Pão Sírio', '100', '70', '30', '5,90', '177,00'])
wr(['Polpa de Açai', '100', '1', '99', '7,10', '639,00'])
wr(['Queijo Vegano', '100', '30', '70', '25,00', '1.750,00'])