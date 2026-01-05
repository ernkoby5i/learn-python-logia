def sprawdzam(n):
    sito = []
    for i in range(0, n + 1):
        sito.append(i)
    print(sito)
    for i in range(2,n+1):
        if sito[i] == i:
            for j in range(i*i, n+1, i):
                sito[j] = i
    return(sito)



n = int(input())
sito = sprawdzam(n)
sito = set(sito)
print(sito)