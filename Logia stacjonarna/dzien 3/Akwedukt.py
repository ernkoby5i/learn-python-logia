from turtle import *

def kwadrat(bok,kolor):
    fillcolor(kolor)
    begin_fill()
    forward(bok)
    left(90)
    forward(bok)
    left(90)
    forward(bok)
    left(90)
    forward(bok)
    left(90)
    end_fill()

def prostokat(bok,kolor):
    fillcolor(kolor)
    begin_fill()
    forward(bok)
    left(90)
    forward(bok*2)
    left(90)
    forward(bok)
    left(90)
    forward(bok*2)
    left(90)
    end_fill()

def dach(bok,kolor):
    fillcolor(kolor)
    begin_fill()
    zero = pos()
    forward(bok)
    left(60)
    forward(bok)
    right(60)
    forward(bok)
    right(60)
    forward(bok)
    left(60)
    forward(bok)
    left(90)
    forward(bok*2)
    left(90)
    forward(bok*4)
    left(90)
    forward(bok*2)

    end_fill()


def dolny(n,bok):
    #n = int(input())

    prostokat(bok, 'lightgrey')
    zero = pos()
    goto(zero[0],zero[1]+bok*2)
    kwadrat(bok, 'firebrick')
    zero = pos()
    goto(zero[0], zero[1] + bok)
    dach(bok, 'lightgrey')
    forward(bok*3)
    left(90)
    forward(bok*3)
    prostokat(bok, 'lightgrey')
    zero = pos()
    goto(zero[0], zero[1] + bok * 2)
    kwadrat(bok, 'firebrick')
    goto(zero)

def srodkowy(n,bok):
    kwadrat(bok,'lightgrey')
    zero = pos()
    goto(zero[0],zero[1]+bok)
    kwadrat(bok, 'firebrick')
    zero = pos()
    goto(zero[0], zero[1] + bok)
    dach(bok, 'lightgrey')
    forward(bok*2)
    left(90)
    forward(bok*3)
    kwadrat(bok, 'lightgrey')
    zero = pos()
    goto(zero[0], zero[1] + bok)
    kwadrat(bok, 'firebrick')
    goto(zero)


def akwedukt():
    n = 6
    bok = 500 / (n+((n-1)*2))
    pu()
    goto(-250, -100)
    zero = pos()
    for i in range(0, n - 1):
        dolny(n, bok)
    goto(zero[0],zero[1]+bok*5)
    zero = pos()
    for i in range(0, n - 1):
        srodkowy(n, bok)
    goto(zero[0], zero[1] + bok * 4)
    bok2 = bok/2
    for i in range(0, (n-1) * 2):
        srodkowy(n, bok2)



speed(0)
akwedukt()
exitonclick()










"""goto(-250,-bok*(x-6))
    for i in range(0,n-1):
        dolny(n,bok)
    goto(-250, -bok * (x-11))
    for i in range(0,n-1):
        srodkowy(n,bok)
    goto(-250, -bok * (x-15))
    bok = bok/2
    for i in range(0,n*2-1):
        srodkowy(n,bok)"""