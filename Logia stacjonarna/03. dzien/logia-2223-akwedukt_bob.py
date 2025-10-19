# https://logia.oeiizk.waw.pl/strony/archiwalne/L23_zadania_e1.pdf

from turtle import *

color_border = "black"
color_kolumna = "lightgrey"
color_sklepipenie = "lightgrey"
color_klocek = "firebrick"

AKWEDUKT_SZEROKOSC  = 500
AKWEDUKT_WYSOKOSC   = 0

def prostokat(x,y,a,b,border_color, fill_color ):
    fillcolor(fill_color)  # jasnoniebieski
    pencolor(border_color)  # obramowanie czarne
    goto(x,y)
    pendown()
    begin_fill()
    forward(a)
    left(90)
    forward(b)
    left(90)
    forward(a)
    left(90)
    forward(b)
    left(90)
    end_fill()
    penup()


def sklepienie(n,x,y,a,border_color, fill_color ):
    fillcolor(fill_color)  # jasnoniebieski
    pencolor(border_color)  # obramowanie czarne
    goto(x,y)
    pendown()
    begin_fill()

    for i in range(n):
        forward(a)
        left(60)
        forward(a)
        right(60)
        forward(a)
        right(60)
        forward(a)
        left(60)
    forward(a)

    # domkniecie sklepienia
    left(90)
    forward(2*a)
    left(90)
    forward(n*a*3+a)
    left(90)
    forward(2 * a)
    left(90)


    end_fill()
    penup()


def oblicz_parametry(n):
    global AKWEDUKT_SZEROKOSC, AKWEDUKT_WYSOKOSC
    a = AKWEDUKT_SZEROKOSC /(3*n+1)
    m = n*2
    b = AKWEDUKT_SZEROKOSC / (3 * m  + 1)
    AKWEDUKT_WYSOKOSC = 5*a+ 4*a + 4*b
    x0 = -AKWEDUKT_SZEROKOSC/2
    y0 = -AKWEDUKT_WYSOKOSC/2
    return a, b, x0, y0




def kolumny(n,x,y,a,b,odstep, border_color,fill_color ):
    """Narysuj n kolmun o boku a,b
       zaczynajac od x,y
       robiac odstep odstep"""
    for i in range(n):
        prostokat(x,y,a,b,border_color, fill_color )
        x = x + a + odstep



def akwedukt(n):

    setup(width=800, height=600)  # rozmiar okna
    speed(0)  # najszybsze rysowanie
    hideturtle()  # ukryj żółwia
    penup()

    (a,b, x0,y0) = oblicz_parametry(n)
    prostokat(x0, y0, AKWEDUKT_SZEROKOSC, AKWEDUKT_WYSOKOSC, "darkblue", "lightblue")
    kolumny(n+1, x0, y0, a, 2*a, 2*a,  color_border, color_kolumna)
    kolumny(n + 1, x0, y0+5*a, a, a, 2 * a, color_border, color_kolumna )
    kolumny(n*2 + 1, x0, y0+5*a+a*4, b, b, 2 * b, color_border, color_kolumna )


    kolumny(n+1, x0, y0+2*a, a, a, 2*a,  color_border, color_klocek)
    kolumny(n + 1, x0, y0+5*a+a, a, a, 2*a, color_border, color_klocek )
    kolumny(n*2 + 1, x0, y0+5*a+a*4+b, b, b, 2*b, color_klocek, color_klocek )

    sklepienie(n,x0, y0+a*3, a, color_border, color_sklepipenie)
    sklepienie(n,x0, y0+a*3+2*a+2*a, a, color_border, color_sklepipenie)
    sklepienie(n*2,x0, y0+a*3+2*a+2*a+2*a+b*2, b, color_border, color_sklepipenie)


    exitonclick()
    return




akwedukt(4)