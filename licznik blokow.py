a , b = input().split()
a = int(a)
b = int(b)
lista2 = input()

lista = []
slownik = {}


for i in lista2:
    lista.append(i)
    if i in slownik:
        slownik[i] = slownik[i]+1
    else:
        slownik[i] = 1
ktory = 0
x = 0
while x<b:
    naj = None
    for i in slownik:
        if naj == None:
            naj = slownik[i]
            ktory = i


        if slownik[i]<naj:
            naj = slownik[i]
            ktory = i


    slownik[ktory]  = slownik[ktory]-1
    if slownik[ktory] == 0:
        del slownik[ktory]
    x = x+1

print(len(slownik))