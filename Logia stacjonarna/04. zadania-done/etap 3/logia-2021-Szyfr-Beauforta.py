lista ,klucz = input().split()
ilelista = len(lista)

ileklucz = len(klucz)

reszta = ilelista-ileklucz
print(lista)
print(ilelista)
print(klucz)
print(ileklucz)


lista2 = []
for i in lista:
    lista2.append(i)
print(lista2)

lista3 = []
for i in lista2:
    pozycja = ord(i) - ord('a')
    odbicie = 25 - pozycja
    lista3.append(chr(odbicie + ord('a')))
print(lista3)


klucz2 = []
for i in klucz:
    klucz2.append(i)

for i in range(0,reszta):
    klucz2.append(klucz[i])
print(klucz2)


lista4 = []
for i in klucz2:
    oile =  ord(i) - 96
    lista4.append(oile)
print(lista4)

for i in range(len(lista3)):
    b = ord(lista3[i]) + lista4[i]
    if b > 122:
        b = b - 26
    print(chr(b), end="")





