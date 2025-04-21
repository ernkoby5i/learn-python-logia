"""
8*. Wypisz N kolejnych liczb, które są zapisane tylko z cyfr 1 i 2. Np. dla N = 7 wypisujemy 1, 2, 11, 12, 21, 22, 111
"""
n = 7
DOBRE_CYFRY = [1,2]

# jezeli liczba sklada sie dobrych cyfr np. 1,2 to funkcja poprawna_liczb zwraca True
# jezeli zawiera inne cyfry  zwraca False
# hint: jezeli znajdziersz choc jedna nieprawidlowa to zwracasz False
def poprawna_liczba(liczba):
    s = str(liczba)
    for c in s:
        if int(c) not in DOBRE_CYFRY:
            return False
    return True


# w petli while iteruj i i wypisuj poprawne liczy
# przerwij petle while po wypisaniu n liczb
def wypisz_n_liczb(n):
    c = 0
    i = 0
    while True:
        i = i + 1
        if poprawna_liczba(i):
            c = c + 1
            print(c, n, i)
        if c >= n:
            break
    return 0



liczba = 121231
print(f"napis {liczba} poprawny: {poprawna_liczba(liczba)}")
wypisz_n_liczb(7)






