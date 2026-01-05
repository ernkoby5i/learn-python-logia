from turtle import *
def kwadrat(bok,kolor):
    pd()
    fillcolor(kolor)
    begin_fill()
    for i in range(0,4):
        forward(bok)
        left(90)

    end_fill()
    forward(bok)
    left(90)
    forward(bok)
    left(90)
    forward(bok)
    left(90)
    right(270)
    pu()

def a(bok):

    goto(0,bok*0)
    kwadrat(bok,'red')
def b(bok):
    goto(0, bok * 1)
    kwadrat(bok, 'red')
def c(bok):
    goto(0, bok * 2)
    kwadrat(bok, 'red')
def d(bok):
    goto(0, bok * 3)
    kwadrat(bok, 'red')
def e(bok):
    goto(0, bok * 4)
    kwadrat(bok, 'red')
def f(bok):
    goto(0, bok * 5)
    kwadrat(bok, 'red')
def g(bok):
    goto(0, bok * 6)
    kwadrat(bok, 'red')
def h(bok):
    goto(0, bok * 7)
    kwadrat(bok, 'red')
def ii(bok):
    goto(0, bok * 8)
    kwadrat(bok, 'red')
def j(bok):
    goto(0, bok * 9)
    kwadrat(bok, 'red')
def k(bok):
    goto(0, bok * 10)
    kwadrat(bok, 'red')
def l(bok):
    goto(0, bok * 11)
    kwadrat(bok, 'red')
def m(bok):
    goto(0, bok * 12)
    kwadrat(bok, 'red')
def n(bok):
    goto(bok, bok * 12)
    kwadrat(bok, 'red')
def o(bok):
    goto(bok, bok * 11)
    kwadrat(bok, 'red')
def p(bok):
    goto(bok, bok * 10)
    kwadrat(bok, 'red')
def q(bok):
    goto(bok, bok * 9)
    kwadrat(bok, 'red')
def r(bok):
    goto(bok, bok * 8)
    kwadrat(bok, 'red')
def s(bok):
    goto(bok, bok * 7)
    kwadrat(bok, 'red')
def t(bok):
    goto(bok, bok * 6)
    kwadrat(bok, 'red')
def u(bok):
    goto(bok, bok * 5)
    kwadrat(bok, 'red')
def v(bok):
    goto(bok, bok * 4)
    kwadrat(bok, 'red')
def w(bok):
    goto(bok, bok * 3)
    kwadrat(bok, 'red')
def x(bok):
    goto(bok, bok * 2)
    kwadrat(bok, 'red')
def y(bok):
    goto(bok, bok * 1)
    kwadrat(bok, 'red')
def z(bok):
    goto(bok, bok * 0)
    kwadrat(bok, 'red')


def siatka(bok,szerokosc):
    pd()
    for j in range(1,szerokosc+1):
        for i in range(0,13):
            kwadrat(bok,'white')

        pu()
        goto(bok*j,0)
        pd()
    pu()


def caly():
    lista = ['a','b','c','d','e','f','g']
    bok = 25
    siatka(bok,len(lista)*2)
    for i in lista:
        if i == 'a':
            zero = pos()
            a(bok)
            goto(zero[0]+bok*2,zero[1])
            continue
        if i == 'b':
            zero = pos()
            b(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 'c':
            zero = pos()
            c(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 'd':
            zero = pos()
            d(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 'e':
            zero = pos()
            e(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 'f':
            zero = pos()
            f(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 'g':
            zero = pos()
            g(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 'h':
            zero = pos()
            h(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 'i':
            zero = pos()
            ii(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 'j':
            zero = pos()
            j(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 'k':
            zero = pos()
            k(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 'l':
            zero = pos()
            l(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 'm':
            zero = pos()
            m(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 'n':
            zero = pos()
            n(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 'o':
            zero = pos()
            o(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 'p':
            zero = pos()
            p(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 'q':
            zero = pos()
            q(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 'r':
            zero = pos()
            r(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 's':
            zero = pos()
            s(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 't':
            zero = pos()
            t(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 'u':
            zero = pos()
            u(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 'v':
            zero = pos()
            v(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 'w':
            zero = pos()
            w(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 'x':
            zero = pos()
            x(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 'y':
            zero = pos()
            y(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue
        if i == 'z':
            zero = pos()
            z(bok)
            goto(zero[0] + bok * 2, zero[1])
            continue



pu()
speed(0)
caly()
exitonclick()