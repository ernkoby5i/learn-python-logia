#f) Powiększa oba boki listy dwukrotnie, z każdej liczby robiąc cztery nowe w
#   kwadracie 2 x 2 (najlepiej to zrozumieć na przykładzie)

def powieksz(lista):
    wynik = []
    for i in lista:
        wiersz = []
        for j in i:
            wiersz += [j, j]
        wynik += [wiersz, wiersz]
    return wynik
