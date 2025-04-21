napis = input()
pismo = input()
n = len(napis)
m = len(pismo)
f = 0
g = 0
if n>m:
    for i in pismo:
        if i != napis[f]:
            g = g+1
        f = f+1
    print(g)
else:
    for i in napis:
        if i != pismo[f]:
            g = g+1
        f = f+1
    print(g)