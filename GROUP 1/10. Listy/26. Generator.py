n = int(input())
c = 1
l = []

for i in range(1, n+1):
    if c%2!=0:
        l.append(i)
        c = c+1
    else:
        l.insert(0,i)
        c = c+1

print(l)