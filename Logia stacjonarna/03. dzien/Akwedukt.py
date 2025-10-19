from turtle import *

def kwadrat(bok,kolor):
    fillcolor(kolor)
    pd()
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
    pu()


def prostokat(bok,kolor):
    pd()
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
    pu()

def dach(bok,kolor):
    pd()
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
    pu()
    forward(bok*2)
    pd()

    end_fill()
    pu()


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


def akwedukt(n):
    o1 = n - 1   # ilosc okien poziom 1
    o3 = 2 * o1  # ilosc okien poziom 3
    bok = 500 / (1+o1*3)
    bok2 = 500 / (1 + o3 * 3)

    hideturtle()
    pu()
    goto(-250, -(5*bok+4*bok+4*bok2)/2)
    zero = pos()
    for i in range(0, n - 1):
        dolny(n, bok)
    goto(zero[0],zero[1]+bok*5)
    zero = pos()
    for i in range(0, n - 1):
        srodkowy(n, bok)
    goto(zero[0], zero[1] + bok * 4)
    #bok2 = bok/2
    #bok2 = 500 / (1+o3*3)
    for i in range(0, (n-1) * 2):
        srodkowy(n, bok2)
    pu()
    goto(-250, -(5 * bok + 4 * bok + 4 * bok2) / 2)
    pd()
    zero = pos()
    goto(zero[0], zero[1]+(bok*9+4*bok2))



speed(0)
akwedukt(8)
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