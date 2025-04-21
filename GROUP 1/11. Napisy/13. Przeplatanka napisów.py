napis = input()
pismo = input()
wynik = []
n = len(napis)
c = 1

for i in range(0, n):

    wynik.append(napis[i])
    wynik.append(pismo[i])


for i in wynik:
    print(i,end='')