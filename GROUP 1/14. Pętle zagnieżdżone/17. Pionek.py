n = int(input())
l2 = list(map(int, input().split()))
najwieksza = None

for krok in range (1,n+1):
    s = 0
    index = 0
    while True:
        if index<=n-1:
            s = s+l2[index]
        else:
            break
        index = index+krok
    if najwieksza is None:
        najwieksza = s
    else:
        if s>najwieksza:
            najwieksza = s


print(najwieksza)






