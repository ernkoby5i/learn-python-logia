# 15. 21.01.2025 https://codeshare.io/w9xzjp Slownik                        [BARDZO WAZNE]
# 2.a. Liczenie częstotliwości występowania liter w tekście - napisz program, która wczyta string składający się z małych liter alfabetu łacińskiego, a następnie,
# korzystając ze słownika, policzy ile razy dana litera w nim wystąpiła, a następnie wypisze ten słownik.

slowo = input()
litery = dict()

for i in slowo:
    if i in litery:
        litery[i] += 1
    else:
        litery[i] = 1
print(litery)