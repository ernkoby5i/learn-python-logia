slowo = "aabbccaa"
slownik = {}

for litera in slowo:
    if litera in slownik:
        slownik[litera] += 1
    else:
        slownik[litera] = 1

print(slownik)
