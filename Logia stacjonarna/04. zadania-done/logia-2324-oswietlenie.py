a,b = input().split()
a = int(a)
b = int(b)
llista = input().split()
lista = []
wl = 0
wy = 0
for i in llista:
    lista.append(int(i))
    print(i)

print(lista)
on = False
for i in lista:
    if i < a:
        if not on:
            on = True
            wl = wl + 1
    elif i > b:
        if on:
            on = False
            wy = wy + 1

print(wl, wy)

