s1 = list(input())
s2 = []
obecna = None

for e in s1:
    if obecna == e:
        continue
    s2.append(e)
    obecna = e

for i in s2:
    print(i,end='')