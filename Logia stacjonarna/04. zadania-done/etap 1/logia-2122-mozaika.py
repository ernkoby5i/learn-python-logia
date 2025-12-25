# https://logia.oeiizk.waw.pl/strony/archiwalne/L22_zadania_e1.pdf
from turtle import *

def kwadrat(z, kolor):
    pd()
    fillcolor(kolor)
    begin_fill()
    forward(z)
    right(90)
    forward(z)
    right(90)
    forward(z)
    right(90)
    forward(z)
    right(90)
    end_fill()
    pu()

def mozajka():
    pd()
    fillcolor('lightblue')
    begin_fill()
    goto(200, 200)
    goto(200, -200)
    goto(-200, -200)
    goto(-200, 200)
    end_fill()

    n = int(input())
    kratki = 0
    kolory = ['green','orange']
    for i in range(2,n+1):
        kratki = kratki+i
    kratki = kratki+kratki+2
    bok = 400/kratki


    for i in range(1):
        zero = pos()
        z = bok * 2
        for i in range(0,n-1):
            kolor = kolory[i%2]
            kwadrat(z,kolor)
            forward(z // 2)
            right(90)
            forward(z // 2)
            left(90)
            PAMIENTAJ = pos()
            z = z + (bok*2)
        goto(zero)
        forward(400)
        right(90)

    for i in range(0,3):
        zero = pos()
        z = bok * 2
        for i in range(0,n-1):
            kolor = kolory[i%2]
            kwadrat(z,kolor)
            forward(z // 2)
            right(90)
            forward(z // 2)
            left(90)
            z = z + (bok*2)
        goto(zero)
        forward(400)
        right(90)


    goto(PAMIENTAJ)

    z = z + (bok * 2)-bok
    kolor = 'green'
    kwadrat(z, kolor)


pu()
speed(0)
goto(-200,200)
mozajka()
exitonclick()