
l = input()
l1 = []

for i in l:
    #print(i)
    x = ord(i)+32
    if ord(i)<=90:
        l1.append(chr(x))
    else:
        l1.append(i)

#print(l1)

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
