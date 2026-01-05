def sprawdzam(liczba):
    if liczba<2:
        return False
    for i in range(2,int(liczba**0.5)+1):
        if liczba%i==0:
            return False
    return True

a = int(input())
czy = sprawdzam(a)
if czy:
    print('tak jest pierwsza')
else:
    print('nie, nie jest pierwsza')