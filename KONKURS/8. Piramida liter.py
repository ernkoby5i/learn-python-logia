n = int(input())
x = n
licznik = 1
for i in range(0,n):
    x = x-1
    print(" " * x,end='')
    for i in range(0,licznik):
        print(chr((n-licznik+i)+65),end='')
    for j in range(licznik - 2, -1, -1):
        print(chr((n - licznik + j) + 65), end='')
    print('')


    licznik = licznik + 1






