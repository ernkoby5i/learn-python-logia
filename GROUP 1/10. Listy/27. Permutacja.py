n = int(input())
l1 = []

for e in range (1, n+1):
    l1.append(0)

l2 = list(map(int, input().split()))

for e in l2:
    if e-1<n:
        l1[e-1] = l1[e-1] + 1

ok = True
for e in l1:
    if e!=1:
        ok = False

if ok:
    print('TAK')
else:
    print('NIE')