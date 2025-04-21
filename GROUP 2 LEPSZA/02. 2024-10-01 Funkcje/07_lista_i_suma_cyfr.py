
"""
7*. Napisz funkcję, której dana jest lista liczb od 1 do 100. W jednym ruchu możemy zamienić liczbę na sumę jej cyfr. Chcemy uzyskać same liczby 1-cyfrowe,
niech nasza funkcja zwróci jak będzie wyglądała wtedy
Np. [33, 92, 1] -> [6, 92, 1] -> [6, 11, 1] -> [6, 2, 1]
"""


def suma_cyfr_jeden_ruch(liczba):
    suma = 0
    while liczba > 0:
        suma = suma + liczba % 10
        liczba = liczba//10
    return suma

def suma_cyfr_wiele_ruchow(liczba):
    while liczba >= 10:
        liczba = suma_cyfr_jeden_ruch(liczba)
    return liczba


krok = 0
l = [2,2, 1,1]
sprawdz_jeszcze_raz = True
while sprawdz_jeszcze_raz:
    sprawdz_jeszcze_raz = False
    for i in range(0,len(l)):
        liczba_stara = l[i]
        liczba_nowa = suma_cyfr_jeden_ruch(liczba_stara)
        if liczba_nowa != liczba_stara:
            l[i] = liczba_nowa
            sprawdz_jeszcze_raz = True
            krok = krok + 1
            print(f'krok = {krok},{l}')


print("KONIEC")
print(l)






