L1 = input()
n = len(L1)
L2 = []
MALE = []
DUZE = []

for i in L1:
    x = ord(i)
    L2.append(x)

for i in L2:
    if i>=97:
        MALE.append(i)
    else:
        DUZE.append(i)
DUZE.sort()
MALE.sort()

WYNIK=[]
WYNIK_OSTATECZNY=[]

for j in MALE:
    found = False
    for i in DUZE:
        if j-32 == i:
            found=True
            break
    if found:
        WYNIK.append(j)
        # w tym miejscu sprawdz czy j jest juz na liscie WYNIK
        # jezeli not znaezliono to dodaj do listy WYNIK
print(WYNIK)

for j in WYNIK:
    Found=False
    for i in WYNIK_OSTATECZNY:
        if j ==i:
            Found = True
    if not Found:
        WYNIK_OSTATECZNY.append(j)

print(len(WYNIK_OSTATECZNY))

