slowo = 'ABCAAEBAGHX'
lista = []
for i in slowo:
    lista.append(i)

ordy = []
for i in lista:
    ordy.append(ord(i))

pop = 0
licznik  = 0
dlugosc = 0

for i in ordy:
    if i < pop:
        pop = i
        licznik = dlugosc - 1
        print('')
        print(' ' * licznik + chr(i), end='')
        dlugosc = licznik + 1
    else:
        print(chr(i), end='')
        pop = i
        dlugosc = dlugosc + 1