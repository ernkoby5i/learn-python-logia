napis = input()
n = len(napis)
maxlen = 0
c = 0
obecna = None
for e in napis:
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