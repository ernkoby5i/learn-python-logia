alf = {'a': 1, 'ą': 2, 'b': 3, 'c': 4, 'ć': 5, 'd': 6, 'e': 7, 'ę': 8,'f': 9, 'g': 10, 'h': 11, 'i': 12, 'j': 13, 'k': 14, 'l': 15,'ł': 16, 'm': 17, 'n': 18, 'ń': 19, 'o': 20, 'ó': 21, 'p': 22,'r': 23, 's': 24, 'ś': 25, 't': 26, 'u': 27, 'w': 28,'y': 29, 'z': 30, 'ź': 31, 'ż': 32}

# wczytaj napis z klawiatury do zmiennej napis
#napis = input()
napis = "abcda"

# zainicjuj zmienne
litera_min = litera_max = napis[0]
liczba_min = liczba_max = alf[napis[0]]



for litera in napis:
    print(f"{litera} - {alf[litera]}")
    liczba = alf[litera]

    if liczba > liczba_max:
        liczba_max = liczba
        litera_max = litera

    if liczba < liczba_min:
        liczba_min = liczba
        litera_min = litera

print(f'MIN:{litera_min} - {liczba_min} MAX:{litera_max} - {liczba_max} ROZNICA: {liczba_max- liczba_min}')

