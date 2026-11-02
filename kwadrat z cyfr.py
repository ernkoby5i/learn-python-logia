a , b = input().split()
a = int(a)
b = int(b)
lista2 = input().split()
lista = []
for i in lista2:
    lista.append(int(i))
lista2 =[]
c = 1
x = True

while len(lista)>0:
    nowy = lista[0]
    sumap = 0
    for i in lista2:
        sumap = sumap+i
    if sumap+lista[0]<=b:
        lista2.append(nowy)
        lista.pop(0)
    elif nowy>b:
        x = False
        break
    else:
        c = c+1
        lista2 = []
        lista2.append(nowy)
        lista.pop(0)

if x:
    print(c)
else:
    print('Stary, nie trac wiary, choc za duze te ciezary,')
    print('Sprobuj jeszcze, poczuj dreszcze,')
    print('Choc wynik ten sam, bo wagi nie zmienia sie gram,')
    print('To probuj do upadlego, dla sportu samego. ')