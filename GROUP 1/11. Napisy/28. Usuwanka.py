napis = input()
lista = list(napis)
# print(napis)
# print(lista)
while len(lista)>=3:
    if lista[0]==lista[-1]:
        lista.pop(0)
        lista.pop(-1)
    else:
        break
# print(lista)
napis = ''.join(lista)
print(napis)
