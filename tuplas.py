class ContaCorrente:

    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposito (self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]" .format(self.codigo, self.saldo)
    

conta = ContaCorrente(15)
print (conta)
conta.deposito (500)
print (conta)

conta2 = ContaCorrente (47685)
conta2.deposito (1000)
print (conta2)

contas = [conta, conta2]

def deposito_todas_contas(contas):
    for conta in contas:
        conta.deposito(100)
print("contas antes:")
print(contas[0], contas[1])
deposito_todas_contas(contas)
print("contas depois:")
print(contas[0], contas[1])

contas.insert(0, 76)

print(contas[0], contas[1],  contas[2])

for conta in contas:
    print(conta)

#tuplas
guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)

conta_do_gui = (15, 1000)

def deposita(conta):
    novo_saldo = conta[1] +100
    codigo = conta[0]
    return (codigo, novo_saldo)

conta_do_gui = deposita(conta_do_gui)
print (conta_do_gui)

usuarios = [guilherme, daniela]
print(usuarios)
usuarios.append(('Paulo', 39, 1979))
print(usuarios)

conta_do_gui = ContaCorrente(15)
conta_do_gui.deposito(500)
conta2 = ContaCorrente(234876)
conta2.deposito(1000)

contas = (conta_do_gui, conta2)

for conta in contas: print(conta)

