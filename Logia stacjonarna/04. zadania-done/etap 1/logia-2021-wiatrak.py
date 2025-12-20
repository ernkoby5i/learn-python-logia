# https://logia.oeiizk.waw.pl/strony/archiwalne/L21_zadania_e1.pdf
from turtle import *
def cz(bok):
    pd()
    START = pos()
    HEAD = heading()

    forward(bok*4)
    pos1 = pos()
    fillcolor('red')
    begin_fill()
    forward(bok)
    right(90)
    forward(bok)
    goto(pos1)
    end_fill()
    left(90)

    forward(bok*3)
    fillcolor('red')
    begin_fill()
    pos1 = pos()
    backward(bok * 2)
    left(90)
    forward(bok * 2)
    goto(pos1)
    end_fill()
    right(90)

    pos1 = pos()
    fillcolor('red')
    begin_fill()
    forward(bok*3)
    right(90)
    forward(bok*3)
    goto(pos1)
    end_fill()
    left(90)

    pd()
    goto(START)
    setheading(HEAD)


def zl(bok):
    pd()
    START = pos()
    HEAD = heading()

    forward(bok*4)
    pos1 = pos()
    fillcolor('green')
    begin_fill()
    forward(bok)
    left(90)
    forward(bok)
    goto(pos1)
    end_fill()
    right(90)

    forward(bok*3)
    fillcolor('green')
    begin_fill()
    pos1 = pos()
    backward(bok * 2)
    right(90)
    forward(bok * 2)
    goto(pos1)
    end_fill()
    left(90)

    pos1 = pos()
    fillcolor('green')
    begin_fill()
    forward(bok*3)
    left(90)
    forward(bok*3)
    goto(pos1)
    end_fill()
    right(90)

    pu()
    goto(START)
    setheading(HEAD)


def caly():
    pu()
    bok = 250/10
    bok1 = 125/10
    for i in range(0,12):
        if i%2==0:
            zl(bok1)
        else:
            cz(bok)
        left(30)

caly()
exitonclick()




