n = int(input())
s1 = list(map(int, input().split()))
i1 = 0
i2 = 1

for i in range(0, n):
    if s1[i] == 1:
        i1 = i
        break

for i in range(1, n+1):
    print("i=", -i)
    if s1[-i] == 1:
        i2 = i
        break

i2 = n-i2
print("i1",i1)
print("i2",i2)
o = i2-i1
print(o)