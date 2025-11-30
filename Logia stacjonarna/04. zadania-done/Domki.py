from turtle import *


def kwadrat(bok,kolor):
    pd()
    fillcolor(kolor)
    begin_fill()
    forward(bok*5)
    left(90)
    forward(bok * 5)
    left(90)
    forward(bok * 5)
    left(90)
    forward(bok * 5)
    left(90)
    end_fill()
    pu()



def czerwone(bok):
    pd()
    zero = pos()
    fillcolor('red')
    begin_fill()

    goto(zero[0]+bok*2,zero[1]+bok*2)
    forward(bok*5)
    zero = pos()
    goto(zero[0]-bok*2,zero[1]-bok*2)
    backward(bok*5)
    end_fill()
    pu()


def szary(bok):
    pd()
    zero = pos()
    fillcolor('grey')
    begin_fill()

    goto(zero[0] + bok * 2, zero[1] + bok * 2)
    right(90)
    forward(bok * 5)
    zero = pos()
    goto(zero[0] - bok * 2, zero[1] - bok * 2)
    backward(bok * 5)
    right(90)
    end_fill()
    right(180)
    pu()


def domek0(bok):
    kwadrat(bok, 'gold')
    zero = pos()
    zero1 = pos()
    goto(zero[0] + bok, zero[1] + bok)
    kwadrat(bok / 5, 'lightblue')

    goto(zero[0] + bok * 3, zero[1] + bok)
    kwadrat(bok / 5, 'lightblue')

    goto(zero[0] + bok * 1, zero[1] + bok * 3)
    kwadrat(bok / 5, 'lightblue')

    goto(zero[0] + bok * 3, zero[1] + bok * 3)
    kwadrat(bok / 5, 'lightblue')

    goto(zero[0], zero[1] + bok * 5)
    czerwone(bok)

    goto(zero[0] + bok * 5, zero[1] + bok * 5)
    szary(bok)


def domek(bok,n):

    for i in range(0,n):
        if i%2==0:

            domek0(bok)
            zero1 = pos()
            goto(zero1[0] - bok * 5, zero1[1] - bok * 5)

        else:

            zero2 = pos()
            goto(zero2[0] + bok * 7, zero2[1] + bok * 2)
            domek0(bok)
            zero2 = pos()
            goto(zero2[0] - (bok * 2), zero2[1] - (bok * 7))




def caly():

    bok = 100/5
    n = 3
    zero1 = pos()
    goto(zero1[0] - bok * 7 / 2, -(bok * 4 + bok / 2))
    for i in range(0,n-1):
        if i%2==0:
            zero1 = pos()
            goto(zero1[0] - bok * 7 / 2, -(bok * 4 + bok / 2))

        else:

            zero2 = pos()
            goto(zero2[0] - bok * 3 / 2, -(bok * 4 + bok / 2))
    domek(bok,n)

pu()
speed(0)
caly()
exitonclick()