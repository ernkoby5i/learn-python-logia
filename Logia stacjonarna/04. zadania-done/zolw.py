

n = int(input())
wynik = 1
for i in range(2,n+1):
    if (i-1) % 12 == 0 and i > 1:
        wynik = wynik-10
    else:
        if i%2==0:
            wynik = wynik+3
        else:
            wynik = wynik-1

print(wynik)