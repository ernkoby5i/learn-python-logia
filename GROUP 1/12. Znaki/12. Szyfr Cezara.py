n = input()
v = []

t = len(n)

for i in range(0,t):

    if n[i]=='x':
        v.append('a')
        continue
    if n[i]=='y':
        v.append('b')
        continue
    if n[i]=='z':
        v.append('c')
        continue
    else:
        x = ord(n[i])
        v.append(chr(x+3))

for i in v:
    print(i,end='')