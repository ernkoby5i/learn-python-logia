from turtle import *
def kwadrat(bok, kolor):
    pd()
    fillcolor(kolor)
    begin_fill()
    for i in range(0,4):
        forward(bok)
        left(90)
    end_fill()
    left(90)
    forward(bok)
    left(270)
    pu()

def pr(bok,kolor):
    pd()
    zero = pos()
    forward(bok)
    left(90)
    forward(bok)
    goto(zero[0],zero[1])
    right(90)
    pu()

def le(bok, kolor):
    pd()
    forward(bok)
    zero = pos()
    backward(bok)
    left(90)
    forward(bok)
    goto(zero[0],zero[1])
    pu()
def gu(bok, kolor):
    pd()
    zero = pos()
    goto(zero[0]+bok/2,zero[1]+bok)
    pu()
def du(bok, kolor):
    pd()
    forward(0)
    pu()

def slup(ile,jaki):
    for i in range(0,ile):
        kwadrat(50,'green')
    if jaki=='P':
        pr(50,'green')
    if jaki=='L':
        le(50, 'green')
    if jaki=='G':
        gu(50, 'green')
    if jaki=="D":
        du(50, 'green')


def caly():
    lista = [5,8,9,3,6,8,1]
    for i in lista:
        zero = pos()
        slup(i,'P')
        goto(zero[0]+50,zero[1])

pu()
speed(0)
caly()
exitonclick()
