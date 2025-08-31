lista = [4,1,2,2,4,1,1,3,7,1,2,3,4]
n = 4
zerowa = [0] * n
licznik = n
d = 0

for i in lista:
    d = d+1
    if zerowa[i-1]==0:
        zerowa[i-1] = 1
        licznik = licznik-1
    if licznik == 0:
        print(d)
        break


