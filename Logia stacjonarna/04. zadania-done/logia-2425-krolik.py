
a = int(input())

llista = input().split()
lista = []
for i in llista:
    lista.append(int(i))

w = 0
for i in lista:
    if i<a:
        w = w+1

suma = 0
if w>0:
    for i in lista:
        x = a
        if i<a:
            x = x-i
            suma = suma+x
else:
    zaj = lista[0]
    for i in lista:
        if i<zaj:
            zaj = i

    for i in lista:
        x = a
        if i==zaj:
            x = i-x
            suma = suma+x
print(suma)

