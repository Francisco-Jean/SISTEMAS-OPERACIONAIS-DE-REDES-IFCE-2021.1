class Carro:

    def __init__(self, consumo):
        self.consumo = consumo
        self.combustivel = 0.0
        self.autonomia = self.consumo * self.combustivel

    def andar(self, km):
            if km <= self.autonomia:
                self.combustivel -= km / self.consumo
                self.autonomia = self.consumo * self.combustivel
                print('\nVocê chegou ao seu destino!\n')
            else:
                print(f'\nCombustível insuficiente para andar {km} quilômetros.\n')

    def obterGasolina(self):
        return self.combustivel

    def adicionarGasolina(self, add):
        self.combustivel += add
        self.autonomia = self.consumo * self.combustivel
        print(f'\nGasolina disponível: {self.combustivel} litros')

car = Carro(10.0)

x = '1'

while x != '0':
    print('\nOlá, o que você deseja fazer com o seu carro?')
    x = input('\n1 - ARDAR (Km)\n2 - VER A GASOLINA DISPONÍVEL (L)\n3 - ABASTECER (L)\nOUTRA TECLA - SAIR\n\nOPÇÃO: ')

    if x == '1':
        car.andar(float(input('\nQuantos quilômetros você deseja andar? ')))
    elif x == '2':
        print(f'\nCasolina atual: {car.combustivel} litros.\n')

    elif x == '3':
        car.adicionarGasolina(float(input('Digite quantos litros de gasolina vai adicionar: ')))
    else:
        x = '0'
        print('\nCarro adicionado na garagem...\nPrograma finalizado...\n')




