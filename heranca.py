from abc import ABCMeta, abstractmethod

class Conta:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposito (self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]" .format(self._codigo, self._saldo)
    
print(Conta(88))

class ContaCorrente(Conta):
    
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupança(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    pass

conta16 = ContaCorrente(16)
conta16.deposito(1000)

conta17 = ContaPoupança(17)
conta17.deposito(1000)

ContaInvestimento(764)
print (ContaInvestimento)

contas = [conta16, conta17]

for conta in contas:
    conta.passa_o_mes()
    print (conta)