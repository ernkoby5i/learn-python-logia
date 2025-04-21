n = int(input())
l1 = []
c = 1
d = 1
x = 0
suma = 0
l1.append(1)
l1.append(1)

for e in range (2, n):
    suma = c + d
    l1.append(suma)
    x = c
    c = suma
    d = x

print(l1)
