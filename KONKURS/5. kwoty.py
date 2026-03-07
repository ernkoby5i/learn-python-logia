X = int(input())
Y = int(input())
Z = int(input())
lista = []
a = X
b = Y
c = Z
d = X+Y
e = X+Z
f = Z+Y
g = X+Y+Z

lista.append(a)
lista.append(b)
lista.append(c)
lista.append(d)
lista.append(e)
lista.append(f)
lista.append(g)
lista_bez = list(set(lista))
print(len(lista_bez))