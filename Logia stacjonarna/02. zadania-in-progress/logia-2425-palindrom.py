tekst = 'abbbaddc'
#tekst = input()
llista = list(tekst)
lista = []
slownik = {}
for i in llista:
    lista.append(i)


for i in lista:
    if i in slownik:
        slownik[i] = slownik[i]+1
    else:
        slownik[i] = 1
print(slownik)

slownik_ost = slownik
le = len(slownik)
naj_nie = 0



for key in slownik.keys():
    print(slownik[key])
    if slownik[key]>naj_nie and slownik[key]%2!=0:
        naj_nie = slownik[key]

print(naj_nie)



print(slownik)