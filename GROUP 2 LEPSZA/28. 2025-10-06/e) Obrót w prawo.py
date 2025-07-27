#e) Obrót w prawo o 90 stopni tej listy, np. dla:

def obrot(lista):
    wynik = []
    for i in range(len(lista)):
        wiersz = []
        for j in range(len(lista)-1, -1, -1):
            wiersz.append(lista[j][i])
        wynik.append(wiersz)
    return wynik
