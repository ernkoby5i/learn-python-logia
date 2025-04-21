l = input()
#l = 'AABAB'
def sprawdz(j,i):
    # j = 0
    # i = 5
    A = 0
    for f in range(j, i + 1):
        if l[f] == "A":
            A = A + 1
        else:
            A = A - 1
    return A

koniec = len(l)

naj = 0
for i1 in range(0,koniec):
    i2 = len(l) - 1
    while i2>i1:
        #print(f'od {i1} do {i2} wynik = ')
        wynik = sprawdz(i1,i2)
        #print(f'od {i1} do {i2} dlugosc {i2-i1+1} wynik = {wynik}')
        dlugosc = i2-i1+1
        if wynik == 0:
            if dlugosc > naj:
                naj = dlugosc
        i2 = i2-1

print(naj)