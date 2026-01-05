tekst = 'abrakadabrahokuspokus'
llista = list(tekst)
slownik = {}

for i in llista:
    if i in slownik:
        slownik[i] += 1
    else:
        slownik[i] = 1

naj_nie = 0
naj_nie_lit = None
for key in slownik:
    if slownik[key] > naj_nie and slownik[key] % 2 != 0:
        naj_nie = slownik[key]
        naj_nie_lit = key
slownik_ost = slownik.copy()

for i in list(slownik.keys()):
    if i == naj_nie and slownik[i] % 2 != 0:
        del slownik_ost[i]
    elif i != naj_nie and slownik[i] % 2 != 0 and naj_nie_lit != i:
        del slownik_ost[i]


suma = 0
for i in slownik_ost:
    suma = suma+slownik_ost[i]



slownik_ost = dict(sorted(slownik_ost.items(), key=lambda x: x[1]))


for key in slownik_ost:
    if slownik_ost[key] % 2 == 0:
        print(key,end="")

for key in slownik_ost:
    if slownik_ost[key]%2!=0:
        print(key*slownik_ost[key],end="")

for key in reversed(list(slownik_ost)):
    if slownik_ost[key] % 2 == 0:
        print(key, end="")