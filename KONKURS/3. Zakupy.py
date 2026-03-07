n = int(input())
lista = []

for i in range(0,3):
    x = input()
    lista.append(len(x))

lista.sort()

c = 0
for i in lista:
    if i>n:
        break
    else:
        n = n-i
        c = c+1
print(c)