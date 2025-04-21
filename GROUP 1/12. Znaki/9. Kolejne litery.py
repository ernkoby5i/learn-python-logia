n = input()
a1 = ord(n[0])
a2 = ord(n[1])
if a1+1==a2 or a1==a2+1:
    print('TAK')
else:
    print('NIE')