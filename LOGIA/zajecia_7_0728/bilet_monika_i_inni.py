#Monika
def bilet(lista):
    prefiks = 0
    maxi = 0

    for i in range(2):
        for j in range(len(lista)):
            prefiks += lista[j]
            maxi = max(maxi, prefiks)
        if maxi == 0:
            break

    return maxi


trasa = [-1,-1]
print(bilet(trasa))

trasa = [3 ,5 ,5 ,2]
print(bilet(trasa))

#Piotr-poprawione

def findString(a):
    best = 0
    current = 0
    for i in a:
        current += i
        best = max(current, best)


    current = best
    for iI in range(len(a)-1, -1, -1):
        current += a[iI]
        best = max(current, best)
    return best


trasa = [-1,-1]
print(findString(trasa))

trasa = [3 ,5 ,5 ,2]
print(findString(trasa))





