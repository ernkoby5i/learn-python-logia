n = int(input())
lista = []
for i in range(0,n):
    c = input()
    c = list(c)
    lista.append(c)



lista2 = []
jest = False
for lista_w_liscie in lista:
    lista3 = []
    for element_w_liscie in lista_w_liscie:
        jest = False
        for element_w_liscie_3 in lista3:
            if element_w_liscie==element_w_liscie_3:
                jest = True
        if jest==False:
            lista3.append(element_w_liscie)

    lista2.append(lista3)



for i in lista2:
    i.sort()
lista2.sort()


for i in lista2:
    lista2[lista2.index(i)] = "".join(i)


slownik = {}
for element in lista2:
    if element in slownik:
        slownik[element] = slownik[element]+1
    else:
        slownik[element] = 1

c = 0
max = 0
for i in slownik:
    if slownik[i]>max:
        max = slownik[i]
print(max)


