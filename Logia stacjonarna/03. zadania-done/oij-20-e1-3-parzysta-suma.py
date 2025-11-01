# https://sio2.mimuw.edu.pl/c/oij20-1/p/par
a,b,c = map(int, input().split())

if (a + b) % 2 == 0:
    liczby = "a+b"
elif (a + c) % 2 == 0:
    liczby = "a+c"
elif (b + c) % 2 == 0:
    liczby = "b+c"
else:
    liczby = "0"


if liczby!='0':
    print("TAK")
    if liczby =="b+c":
        print(f'b = {b} c = {c}')
    elif liczby == "a+c":
        print(f'a = {a} c = {c}')
    elif liczby == "a+b":
        print(f'a = {a} b = {b}')
else:
    print('NIE')