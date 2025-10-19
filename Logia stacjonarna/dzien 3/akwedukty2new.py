from turtle import *

WYSOKOSC = 0
SZEROKOWSC = 500

def oblicz_parametry(o1):
    global WYSOKOSC, SZEROKOWSC
    a = 500 / (o1*3+1)
    o2 = o1*2
    b = 500 / (o2*3+1)
    szerokosc = o1*3*a+a
    WYSOKOSC = 5*a + 4*a +4*b

    print(f'a = {a}     o2 = {o2}      b = {b}       szerokosc = {szerokosc}         wysokosc = {WYSOKOSC}')
    x0 = -szerokosc/2
    y0 = -WYSOKOSC/2
    return a,b,x0,y0

def kolumny(x,y,a,b,kolor,n):
    for i in range(0,n):
        prostokat(x,y,a,b,kolor)
        x = x+3*a

    return

def sklepienie(x,y,bok,n,kolor):
    goto(x,y)
    pd()
    fillcolor(kolor)
    begin_fill()
    for i in range(0,n-1):
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
    forward(SZEROKOWSC)
    left(90)
    forward(bok*2)
    left(90)
    end_fill()
    pu()

def prostokat(x,y,bok1,bok2,kolor):
    fillcolor(kolor)

    goto(x,y)
    pd()
    begin_fill()
    forward(bok1)
    left(90)
    forward(bok2)
    left(90)
    forward(bok1)
    left(90)
    forward(bok2)
    left(90)
    end_fill()
    pu()

def akwedukt(n):
    pu()
    hideturtle()
    (bok1,bok2,x0,y0) = oblicz_parametry(n-1)
    prostokat(x0,y0,SZEROKOWSC,WYSOKOSC,'lightblue')
    kolumny(x0,y0,bok1,2*bok1,'lightgrey',n)
    kolumny(x0, y0+2*bok1, bok1, bok1, 'red', n)
    kolumny(x0, y0 + 5 * bok1, bok1, bok1, 'lightgrey', n)
    kolumny(x0, y0 + 6 * bok1, bok1, bok1, 'red', n)
    kolumny(x0, y0 + 9 * bok1, bok2, bok2, 'lightgrey', n*2-1)
    kolumny(x0, y0 + 9 * bok1+bok2, bok2, bok2, 'red', n * 2 - 1)
    sklepienie(x0, y0+bok1*3, bok1, n, 'lightgrey')
    sklepienie(x0, y0 + bok1 * 7, bok1, n, 'lightgrey')
    sklepienie(x0, y0 + bok1 * 9+2*bok2, bok2, n*2-1, 'lightgrey')


    return



speed(0)
akwedukt(9)
exitonclick()