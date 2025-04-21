# 15. 21.01.2025 https://codeshare.io/w9xzjp Slownik                        [BARDZO WAZNE]
# 4. Na wejściu podano napisy. Znajdź ten, który występuje największą liczbę razy. Nie ma dwóch napisów o tej samej liczbie wystąpień.
#
# Wejście:
# W pierwszym wierszu podano liczbę napisów. W kolejnych wierszach znajdują się napisy złożone z małych liter.
# Liczba napisów nie przekracza 100,000, a suma długości napisów nie przekracza 500,000 liter.
#
# Wyjście:
# Najczęściej występujący napis oraz liczba jego wystąpień.

slownik = dict()
N =int(input())
for i in range(N):
    g = input()
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