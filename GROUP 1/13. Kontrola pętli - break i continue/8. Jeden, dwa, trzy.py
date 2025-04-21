n = int(input())
s1 = list(map(int, input().split()))
F1 = False
F2 = False
F3 = False

dlugosc = 0

for i in range (0,n):
    if s1[i]==1:
        F1 = True
    if s1[i]==2:
        F2 = True
    if s1[i]==3:
        F3 = True

    if F1 and F2 and F3:
        dlugosc = i
        break
print(dlugosc+1)
