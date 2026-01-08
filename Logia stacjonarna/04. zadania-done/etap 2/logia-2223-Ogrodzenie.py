n = int(input())
liczby = input().split()
lista = []
for i in liczby:
    lista.append(int(i))

naj = 0
index = None
for i in range(0,n):
    if lista[i]>naj:
        naj = lista[i]
        index = i
lista.pop(index)

naj = 0
index = None
for i in range(0,n-1):
    if lista[i]>naj:
        naj = lista[i]
        index = i
lista.pop(index)

suma = 0
for i in lista:
    suma = suma+i

print(suma)






