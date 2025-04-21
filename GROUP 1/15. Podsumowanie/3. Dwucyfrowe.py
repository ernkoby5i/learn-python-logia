n = int(input())
m = int(input())
c = 0

for i in range(n,m+1):
    if i>9 and i<100:
        c = c+1

print(c)