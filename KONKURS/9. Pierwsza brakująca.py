#tekst = input()
tekst = '1011123456789'
lista = []
for i in range(1,len(tekst)+1):
    print(i)
    znalezione_liczby = []
    znalezione_liczby_set = set()
    for j in range(0,len(tekst)-i+1):
        #print(f'j = {j} dla i = {i}')
        start = j
        d = i
        #print('Wypisuje kolejną liczbe')
        #print(tekst[start:start + d])
        znalezione_liczby.append(tekst[start:start + d])
        znalezione_liczby_set.add(tekst[start:start + d])
    print(znalezione_liczby)
    print(znalezione_liczby_set)
    for liczba in range(10**(i-1),10**i):
        znaleziono = False
        liczba_str = str(liczba)
        #for element in znalezione_liczby:
        #    if element==liczba:
        #        znaleziono = True
        #        break
        if liczba_str in znalezione_liczby_set:
            znaleziono = True
        if znaleziono == False:
            break

    if znaleziono == False:
        print(liczba_str)
        break



