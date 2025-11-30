from turtle import *
def trojkat(bok,kolor):
    pd()
    fillcolor(kolor)
    begin_fill()
    for _ in range(3):
        forward(bok)
        left(120)
    end_fill()
    pu()




def figura(bok, liczba):
    if liczba>=8:
        trojkat(bok,'green')
        liczba = liczba%8
    else:
        trojkat(bok, 'white')

    forward(bok)
    left(60)

    if liczba>=4:
        trojkat(bok,'green')
        liczba = liczba%4
    else:
        trojkat(bok, 'white')

    forward(bok)
    right(180)

    if liczba>=2:
        trojkat(bok,'green')
        liczba = liczba%2
    else:
        trojkat(bok, 'white')

    forward(bok)
    left(120)
    forward(bok)
    left(60)

    if liczba>=1:
        trojkat(bok,'green')
        liczba = liczba%1
    else:
        trojkat(bok, 'white')

    right(60)




def caly():
    bok = 26
    n = 3457345
    n = str(n)
    goto(-(len(n))*26,-13)
    lista = []
    for i in n:
        lista.append(int(i))
    print(lista)

    for x in lista:
        figura(bok, x)
    goto(0,0)
    dot(80)


speed(0)
pu()
caly()
exitonclick()