WYNIK = input()
WYNIK_OSTATECZNY=[]

for j in WYNIK:
    Found=False
    for i in WYNIK_OSTATECZNY:
        if j ==i:
            Found = True
    if not Found:
        WYNIK_OSTATECZNY.append(j)

print(len(WYNIK_OSTATECZNY))
