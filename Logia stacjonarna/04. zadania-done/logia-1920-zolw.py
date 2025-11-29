# https://logia.oeiizk.waw.pl/strony/archiwalne/L20_zadania_e1.pdf
from turtle import*
import math

def nasiono(bok2,bok,kolor):
    fillcolor(kolor)
    begin_fill()
    pd()
    zero = pos()
    goto(zero[0]+bok2,zero[1]+bok2)
    forward(bok * 2)
    zero = pos()
    goto(zero[0] + bok2, zero[1] - bok2)
    forward(bok)
    left(180)
    forward(bok)
    zero = pos()
    goto(zero[0] - bok2, zero[1] - bok2)
    forward(bok * 2)
    zero = pos()
    goto(zero[0] - bok2, zero[1] + bok2)
    end_fill()
    pu()

def gorny(bok2,bok,kolor):
    fillcolor(kolor)
    begin_fill()
    pd()

    left(180)
    forward(bok)
    zero = pos()
    goto(zero[0] + bok2, zero[1] + bok2)
    zero = pos()
    goto(zero[0] + bok2, zero[1] + bok2)
    left(90)
    forward(bok)
    zero = pos()
    goto(zero[0] + bok2, zero[1] + bok2)
    zero = pos()
    goto(zero[0] - bok2, zero[1] - bok2)
    left(90)
    forward(bok)
    zero = pos()
    goto(zero[0] - bok2, zero[1] - bok2)
    zero = pos()
    goto(zero[0] - bok2, zero[1] - bok2)
    left(90)
    forward(bok)
    right(90)
    end_fill()
    pu()

def dul(bok2,bok,kolor):
    fillcolor(kolor)
    begin_fill()
    pd()

    left(180)
    forward(bok)
    zero = pos()
    goto(zero[0] + bok2, zero[1] - bok2)
    zero = pos()
    goto(zero[0] + bok2, zero[1] - bok2)
    right(90)
    forward(bok)
    zero = pos()
    goto(zero[0] + bok2, zero[1] - bok2)
    zero = pos()
    goto(zero[0] - bok2, zero[1] + bok2)
    right(90)
    forward(bok)
    zero = pos()
    goto(zero[0] - bok2, zero[1] + bok2)
    zero = pos()
    goto(zero[0] - bok2, zero[1] + bok2)
    right(90)
    forward(bok)
    left(90)



    end_fill()
    pu()

def caly():
    n = 7
    A = (250/n)/2
    a = A/math.sqrt(2)

    goto(-750/2,0)
    pd()
    forward(500)
    zero = pos()
    nasiono(a,A,'gold')
    for i in range(0,n):
        forward(2 * A)
        gorny(a, A, 'gold')
    goto(zero)
    for i in range(0, n):
        forward(2 * A)
        dul(a, A, 'gold')




pu()
caly()
exitonclick()