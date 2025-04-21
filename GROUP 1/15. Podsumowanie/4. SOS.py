n = input()
s2 = 0
o2 = 0
sos = 0

for i in n:
    if i == 'S':
        s2 = s2+1
    elif i == 'O':
        o2 = o2+1

for i in n:
    if o2>=1 and s2>=2:
        s2 = s2-2
        o2 = o2-1
        sos = sos+1
    else:
        break

print(sos)