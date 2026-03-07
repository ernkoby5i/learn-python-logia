n = input()
lista = []
for i in n:
    lista.append(int(i))

for i in range(0,len(lista)-3):
    lista[i] = '*'

for i in lista:
    print(i,end='')