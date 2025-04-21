lis = input()
for i1 in lis:
    if ord(i1)>=97 and ord(i1)<=122:
        kod_a = ord(i1) - 32
        print(chr(kod_a),end='')
    elif ord(i1)>=65 and ord(i1)<=90:
        kod_b = ord(i1) + 32
        print(chr(kod_b), end='')

