N = int(input())
liczby = list(map(int, input().split()))
koniec = -1
c = 0

for i in range(0, N):
        if liczby[i]==0:
                c = c+1
        if c==3:
                koniec = i+1
                break
print(koniec)