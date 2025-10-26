from os import startfile
from turtle import *


def kwadrat(kolor, bok):
    zero = pos()
    fillcolor(kolor)
    begin_fill()
    goto(zero[0] - bok // 2, zero[1] + bok // 2)
    goto(zero[0] - bok, zero[1])
    goto(zero[0] - bok // 2, zero[1] - bok // 2)
    goto(zero)
    end_fill()
    goto(zero[0] - bok, zero[1])

def sierodekup(kolor,bok):
    zero = pos()
    fillcolor(kolor)
    begin_fill()
    goto(zero[0] - bok, zero[1])
    goto(zero[0], zero[1]+bok)
    goto(zero[0] + bok//2, zero[1] + bok//2)
    goto(zero)
    end_fill()

def obramowkaup(kolor,bok):
    zero = pos()
    fillcolor(kolor)
    begin_fill()
    goto(zero[0] + bok//2, zero[1])
    goto(zero[0] - bok, zero[1] + (bok+bok//2))
    goto(zero[0] - (bok * 2+(bok//2)), zero[1])
    goto(zero[0] - (bok * 2 ), zero[1])
    goto(zero[0] - bok, zero[1] + bok)
    goto(zero)
    end_fill()

def obramowkadown(kolor,bok):
    zero = pos()
    fillcolor(kolor)
    begin_fill()
    goto(zero[0] + bok // 2, zero[1])
    goto(zero[0] - bok, zero[1] - bok - bok // 2)
    goto(zero[0] - (bok * 2 + (bok // 2)), zero[1])
    goto(zero[0] - (bok * 2), zero[1])
    goto(zero[0] - bok, zero[1] - bok)
    goto(zero)
    end_fill()


def caly():
    pu()
    n = 1
    dlugosc = 600 // n
    bok = dlugosc // 6
    for i in range (0,n):
        if i>=1:
            goto(zero[0] + (bok + bok // 2), zero[1] + (bok + bok // 2))
        zero = pos()
        for j in range (0,n-i):
            zero2 = pos()
            kwadrat('olivedrab4', bok)
            sierodekup('darkgoldenrod1', bok)
            goto(zero2)
            obramowkaup('indianred1', bok)
            goto(zero2)
            obramowkadown('darkgoldenrod1', bok)
            forward(bok * 3)
        goto(zero)






caly()
exitonclick()