from random import *

def definirConta():
    numero = randint(1,9) * 1000 + randint(0,9) * 100 + randint(0,9) * 10 + randint(0,9)
    return numero

class conta:
    def __init__(self, numconta):
        self._numconta = numconta
        self._saldo = 1000

    def depositar(self, valor):
        self._saldo += valor

    def retirar(self, quantia):
        self._saldo -= quantia

    def getNumconta(self):
        return self._numconta

    def getSaldo_c(self):
        return self._saldo
    
class cliente:

    def __init__(self, nome, cpf, email, senha):
        self.conta = conta(definirConta())
        self._nome = nome
        self._cpf = cpf
        self._email = email
        self._senha = senha

    def getConta(self):
        return self.conta.getNumconta()
        
    def getSaldo(self):
        return self.conta.getSaldo_c()

    def getNome(self):
        return self._nome

    def getCpf(self):
        return self._cpf

    def getEmail(self):
        return self._email

    def getSenha(self):
        return self._senha