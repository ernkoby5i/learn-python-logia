s1 = list(input())
s2 = []
n = len(s1)


for e1 in s1:
    isFound = False

    # przeszukaj
    for e2 in s2:
        if e1 == e2:
            isFound = True
            print("juz mamy " + e1)

    # sprawdz czy znalazl
    if not isFound:
        s2.append(e1)
        print("dodaje " + e1)

print(s1)
print(s2)
if len(s2)>2:
    print('NIE')
else:
    print('TAK')

