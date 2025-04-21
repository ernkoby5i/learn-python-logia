n = input()
v = []
c = 1

for i in n:
    if c%2!=0:
        if ord(i)>=97:
            print(ord(i))
            v.append(ord(i)-32)
        else:
            v.append(ord(i))

    else:
        if ord(i) <= 90:
            print(ord(i))
            v.append(ord(i) + 32)
        else:
            v.append(ord(i))
    c = c+1
print(v)

for i in v:
    print(chr(i),end='')