# 15. 21.01.2025 https://codeshare.io/w9xzjp Slownik                        [BARDZO WAZNE]
# 1*. Oblicz liczbę wystąpień każdego słowa w podanym napisie. Wielkość liter nie ma znaczenia.
#
# Wejście:
# Napis składający się z małych i wielkich liter oraz spacji.
#
# Wyjście:
# Dla każdego słowa, w kolejności z wejścia, wypisz ile razy ono wystąpiło. Każde słowo na wyjściu powinno wystąpić tylko raz. Słowa zapisuj małymi literami.
#
#
# Przykłady:
# Wejście
# Programowanie jest fajne fajne
#
# Wyjście
# programowanie 1
# jest 1
# fajne 2

zdanie = input()
slowa = zdanie.split()
slownik = dict()

for slowo in slowa:
    slowo = slowo.lower()
    if slowo in slownik:
        slownik[slowo] += 1
    else:
        slownik[slowo] = 1
print(slownik)

