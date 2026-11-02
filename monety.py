n = int(input())
licznik = 0


while n//5>0:
    n = n-5
    licznik = licznik+1

if n%2==0:
    licznik = licznik + n//2
    print(licznik)
else:
    licznik = (licznik+1)+((n+1)//2)
    print(licznik)