N = int(input())
liczby = list(map(int, input().split()))


for l in liczby:
     print(l, end=' ')
     if l < 0:
        break

#for i in range (0,N):
#    print(liczby[i], end=' ')
#    if i <= 0:
#        break