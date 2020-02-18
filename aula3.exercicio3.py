import random as rd
contador = 1
lista = []
item = int(input("Quantos itens aleatorios voce quer?"))
while contador <= item:
    lista.append (rd.randrange(0,1000))
    contador = contador + 1
print (lista)
print("Máx:" , max(lista))
print("Mín:" , min(lista))