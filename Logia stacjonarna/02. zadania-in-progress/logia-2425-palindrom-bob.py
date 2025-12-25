tekst = 'abrakadabrahokuspokus'
llista = list(tekst)
slownik = {}

for i in llista:
    if i in slownik:
        slownik[i] += 1
    else:
        slownik[i] = 1

suma  = 0
polowa = ""
srodkowa = 0
srodkowa_litera = ""
for key in slownik:
    print(f'{key} = {slownik[key]}')
    if (slownik[key] % 2 !=0) and  (srodkowa==0):
        srodkowa = 1
        srodkowa_litera = key

    ile_liter_wziac =    (slownik[key] // 2) * 2
    suma = suma +  ile_liter_wziac
    polowa = polowa + key * (ile_liter_wziac//2)

print(polowa)

print(srodkowa_litera)
caly_napis = polowa + srodkowa_litera + polowa[::-1]
print(caly_napis)

