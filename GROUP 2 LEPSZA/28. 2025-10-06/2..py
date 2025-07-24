# Napisz funkcję wygladz(macierz), która dla każdej komórki w macierzy tworzy nową komórkę będącą sumą wartości
# z niej samej oraz wszystkich jej (maksymalnie ośmiu) sąsiadów w oryginale. Jeśli komórka leży na krawędzi
# lub w rogu, bierzesz pod uwagę tylko istniejące sąsiednie komórki. Wynikiem działania
# funkcji jest nowa macierz o tych samych wymiarach, w której każdy element to właśnie ta lokalna suma.

def wygladz(macierz):
    wynik = []
    for i in range(len(macierz)):
        wiersz = []
        for j in range(len(macierz[0])):
            suma = 0
            for y in range(-1, 2): # wartości -1,0,1
                for x in range(-1, 2): # wartości -1,0,1
                    if 0 <= j+x < len(macierz[0]) and 0 <= i+y < len(macierz):
                        suma += macierz[i+y][j+x]
            wiersz.append(suma)
        wynik.append(wiersz)
    return wynik
