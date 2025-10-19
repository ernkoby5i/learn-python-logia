#n = int(input())
n = 4
#p = int(input())
p = 3
podstawa = n
kamykiT = 0

def mozna_zrobic_K(kamykiT):
    """funkcja zwraca:
       true - jezeli z tyh kamykow mozna zrobic prostokat
       false - jezeli jakis warunek nie jet spelniony
    """
    mozna = True
    if kamykiT % p != 0:
        mozna = False
    else:
        m = kamykiT // p
        if not m >= n:
            mozna = False
    return mozna


# main
for i in range(1,n+1):
    kamykiT = kamykiT + i

while not mozna_zrobic_K(kamykiT):
    podstawa = podstawa+1
    kamykiT = kamykiT+podstawa

m = kamykiT // p
print(f'wynik = dlugi bok prostokata = {m} krotki = {p} ilosc kamykow w srodku = {kamykiT}')






