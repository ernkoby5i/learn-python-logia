l1 = [9]
l2 = []
for e1 in l1:
    found = False
    for e2 in l2:
        if e1 == e2:
            found = True
    if found == False:
        l2.append(e1)

print(len(l2))



