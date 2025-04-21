list = input()
naj = 0
for i in list:
    if ord(i)>naj and ord(i)<=57 and ord(i)>=48:
        naj = ord(i)
print(chr(naj))