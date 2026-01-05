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
    fillcolor(kolor)
    begin_fill()
    zero = pos()
    forward(bok)
    left(90)
    forward(bok)
    goto(zero[0],zero[1])
    right(90)
    end_fill()
    pu()

def le(bok, kolor):
    pd()
    fillcolor(kolor)
    begin_fill()
    forward(bok)
    zero = pos()
    backward(bok)
    left(90)
    forward(bok)
    goto(zero[0],zero[1])
    right(90)
    end_fill()
    pu()
def gu(bok, kolor):
    pd()
    fillcolor(kolor)
    begin_fill()
    zero = pos()
    goto(zero[0]+bok/2,zero[1]+bok)
    goto(zero[0]+bok,zero[1])
    goto(zero[0],zero[1])
    end_fill()
    pu()
def du(bok, kolor):
    pd()
    fillcolor(kolor)
    begin_fill()
    zero = pos()
    left(90)
    forward(bok)
    goto(zero[0]+bok/2,zero[1]+bok/5)
    goto(zero[0] + bok, zero[1] + bok)
    goto(zero[0] + bok, zero[1])
    goto(zero[0], zero[1])
    right(90)
    end_fill()
    pu()

def slup(ile,jaki):
    for i in range(0,ile):
        kwadrat(50,'light green')
    if jaki=='P':
        pr(50,'light grey')
    if jaki=='L':
        le(50, 'light grey')
    if jaki=='G':
        gu(50, 'light grey')
    if jaki=="D":
        du(50, 'light grey'
               '')


def caly():
    lista = [5,8,9,3,6,8,1]
    goto(-(len(lista)/2)*50,0)
    c = 0
    for i in range(0,len(lista)):

        if i!=0:
            if i==len(lista)-1:
                srodek = lista[i]
                lewy = lista[i - 1]
                prawy = 0
            else:
                lewy = lista[i - 1]
                prawy = lista[i + 1]
                srodek = lista[i]
        else:
            lewy = 0
            prawy = lista[i + 1]
            srodek = lista[i]



        if srodek > lewy and srodek > prawy:
            c = 'G'

        elif lewy > srodek and prawy <= srodek:
            c = 'L'

        elif prawy > srodek and lewy <= srodek:
            c = 'P'

        elif lewy > srodek and prawy > srodek:
            c = 'D'

        else:
            c = None

        zero = pos()
        slup(lista[i],c)
        goto(zero[0]+50,zero[1])

pu()
speed(0)
caly()
exitonclick()
