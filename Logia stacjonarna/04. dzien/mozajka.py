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
    n = 4
    kratki = 0
    kolory = ['green','orange']
    for i in range(2,n+1):
        kratki = kratki+i
    kratki = kratki+kratki+2
    bok = 400/kratki


    for i in range(0,4):
        zero = pos()
        z = bok * 2
        for i in range(0,n-1):
            kolor = kolory[i%2]
            kwadrat(z,kolor)
            forward(z // 2)
            right(90)
            forward(z // 2)
            left(90)
            z = z + bok + (2 * bok)
        goto(zero)
        forward(600)
        right(90)

pu()
goto(-200,200)
mozajka()
exitonclick()