N = int(input())

ile_jedynek = 0
ile_dwojek = 0

for i in range(0,N):
    waga = int(input())

    if waga == 1:
        ile_jedynek = ile_jedynek + 1
    else:
        ile_dwojek = ile_dwojek + 1

worki = 0

while ile_jedynek > 0 and ile_dwojek > 0:
    worki = worki + 1
    ile_jedynek = ile_jedynek - 1
    ile_dwojek = ile_dwojek - 1

while ile_jedynek >= 3:
    worki = worki + 1
    ile_jedynek = ile_jedynek - 3

print(worki)





