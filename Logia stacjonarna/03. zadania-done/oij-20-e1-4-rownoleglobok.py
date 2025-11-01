# https://sio2.mimuw.edu.pl/c/oij20-1/p/row
wysokosc,szerokosc = map(int, input().split())

for i in range(0,wysokosc):
    print(i * ' ',end="")
    print(szerokosc*'*')