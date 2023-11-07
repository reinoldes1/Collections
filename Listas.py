idades = [39, 30, 27, 18]

print (idades)

print (len (idades))

print (idades [3])

idades.append (15)

print (idades)

for idade in idades:
    print (idade)

idades.remove(30)

print (idades)

print (28 in idades)

if 15 in idades:
    idades.remove(15)
    print(idades)

if 27 in idades:
    idades.insert (0, 20)
    print (idades)

if 20 in idades:
    idades.extend([27,19])
    print (idades)

idades_ano_que_vem = []

# Dessa forma o codigo anterior da bug
#for idade in idades:
#    idades_ano_que_vem.append(idade+1)
#    print (idades_ano_que_vem)

print ([(idade+1) for idade in idades])

print (sorted(idades))
print (idades)

print ([(idade) for idade in idades if idade > 21])

def faz_processamento_de_visualizacao(lista = None):
    if lista == None:
        lista = list()
    print(len(lista))
    print(lista)
    lista.append(13)