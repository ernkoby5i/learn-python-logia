# 4. Danych jest N napisów, ponumerowanych od 0. Dla
# każdego z napisów, wypisz numer jego poprzedniego wystąpienia w ciągu.
# Jeśli napis wystąpił pierwszy raz, wypisz -1.
#
# Wejście:
# W pierwszym wierszu liczba napisów. W kolejnych wierszach po jednym napisie.
#
# Wyjście:
# Dla każdego napisu, numer poprzedniego wystąpienia.

"""
5
0 abba
1 las
2 abba
3 abba
4 las

"""
N = int(input())

slownik = dict()

for i in range(N):
    napis = input()
    if napis in slownik:
        print(slownik[napis])
    else:
        print(-1)
    slownik[napis] = i

