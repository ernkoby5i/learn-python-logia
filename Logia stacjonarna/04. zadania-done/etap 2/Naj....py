napis = input()
napis2 = []
liczby = []
alf = {'a': 1, 'ą': 2, 'b': 3, 'c': 4, 'ć': 5, 'd': 6, 'e': 7, 'ę': 8,'f': 9, 'g': 10, 'h': 11, 'i': 12, 'j': 13, 'k': 14, 'l': 15,'ł': 16, 'm': 17, 'n': 18, 'ń': 19, 'o': 20, 'ó': 21, 'p': 22,'r': 23, 's': 24, 'ś': 25, 't': 26, 'u': 27, 'w': 28,'y': 29, 'z': 30, 'ź': 31, 'ż': 32}

for i in napis:
    napis2.append(i)
for litera in napis:
    liczby.append(alf[litera])


najD = liczby[0]
najB = liczby[0]
Imin = 0
Imax = 0
c = 0

for i in liczby:
    if i>najD:
        najD = i
        Imax = c
    if i<najB:
        najB = i
        Imin = c
    c = c+1

print(napis2[Imax],napis2[Imin],najD-najB)
