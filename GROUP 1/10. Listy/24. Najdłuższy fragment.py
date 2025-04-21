#n = int(input())
#l1 = list(map(int, input().split()))
l1 = [5, 1, -2, -2, 0, 5, -5, 1, 1, 1, 1]
maxlen = 0
c = 0
obecna = None
for e in l1:
    if obecna == None:
        obecna = e
        c = 1
        maxlen = 1
        continue

    if obecna == e:
        c = c+1
        if c > maxlen:
            maxlen = c
    else:
        c = 1
        obecna = e

print(maxlen)