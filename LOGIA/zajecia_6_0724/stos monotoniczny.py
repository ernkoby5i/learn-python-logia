#m = int(input())
m = 7
w = 0
#nasza_lista = list(map(int, input().split()))
nasza_lista = [7, 1, 5, 3, 2, 6, 4]
Stos = []
stos_indexow = []

Stos.append(nasza_lista[0])
stos_indexow.append(0)

for i in range(1,len(nasza_lista)):

    a = len(Stos)-1
    if nasza_lista[i]<Stos[a]:
        Stos[a]=nasza_lista[i]
        stos_indexow[a]=i
    else:
        Stos.append(nasza_lista[i])
        stos_indexow.append(w)

bajtek_skoki = []
bajtek_index = -1
for i in range(0,len(stos_indexow)):
    bajtek_nowy_index = stos_indexow[i]
    skok = bajtek_nowy_index-bajtek_index
    bajtek_skoki.append(skok)
    bajtek_index = bajtek_nowy_index



wynik = 0
for i in range(0,len(bajtek_skoki)):
    wynik = wynik+bajtek_skoki[i]*Stos[i]


print(wynik)

#7
#7 1 5 3 2 6 4

