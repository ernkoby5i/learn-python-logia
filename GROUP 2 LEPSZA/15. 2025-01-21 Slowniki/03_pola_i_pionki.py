# 15. 21.01.2025 https://codeshare.io/w9xzjp Slownik                        [BARDZO WAZNE]
# 3. Dana jest plansza, złożona z pól ułożonych w rzędzie. Na planszy postawionych zostało N pionków. Dla każdego z nich mamy podane pole, na którym został postawiony.
# Znajdź pole, na którym zostało postawione najwięcej pionków. Wypisz liczbę pionków znajdujących się na tym polu. Do rozwiązania użyj słownika.
#
# Wejście:
# W pierwszym wierszu podano liczbę pionków. W kolejnych wierszach znajdują się liczby oznaczające numery pól, na których postawione zostały pionki.
# Pola mogą przyjmować numery z zakresu od -100,000,000 do 100,000,000.
#
# Wyjście:
# Liczba pionków na polu, na którym znajduje się ich najwięcej.
slownik = dict()
N =int(input())
for i in range(N):
    g = int(input())
    if g in slownik:
        slownik[g] += 1
    else:
        slownik[g] = 1




najwieksza_wartosc = 0
naj_klucz = None
for klucz, wartosc in slownik.items():
    print(f"klucz: {klucz}, wartosc:{wartosc}")
    if wartosc > najwieksza_wartosc:
        najwieksza_wartosc = wartosc
        naj_klucz = klucz



print(slownik)
print(f"klucz: {naj_klucz}, najwieksza wartosc:{najwieksza_wartosc}")
