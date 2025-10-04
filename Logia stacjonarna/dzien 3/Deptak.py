from turtle import *
a = 30
b = a
def prawy_jasny(b):
    kolor = 'light sky blue'
    fillcolor(kolor)
    begin_fill()
    forward(b)
    right(135)
    forward(b//2)
    right(45)
    forward(b)
    right(135)
    forward(b // 2)
    right(45)
    forward(b)
    end_fill()

def prawy_ciemny(b):
    kolor = 'royal blue'
    fillcolor(kolor)
    begin_fill()
    forward(b)
    right(135)
    forward(b//2)
    right(45)
    forward(b)
    right(135)
    forward(b // 2)
    right(45)
    forward(b)
    end_fill()


def lewy_jasny(b,lista):
    kolor = 'light sky blue'
    fillcolor(kolor)
    begin_fill()
    forward(b)
    d = pos()
    right(45)
    forward(b//2)
    e = pos()
    right(135)
    forward(b)
    right(45)
    forward(b // 2)
    right(135)
    forward(b)
    end_fill()
    kolor = 'royal blue'
    fillcolor(kolor)
    begin_fill()
    forward(int(b / 1.41))
    goto(e)
    goto(d)
    end_fill()
    forward(int(b / 1.41))

def lewy_ciemny(b,lista):
    kolor = 'royal blue'
    fillcolor(kolor)
    begin_fill()
    forward(b)
    d = pos()
    right(45)
    forward(b//2)
    e = pos()
    right(135)
    forward(b)
    right(45)
    forward(b // 2)
    right(135)
    forward(b)
    end_fill()
    kolor = 'light sky blue'
    fillcolor(kolor)
    begin_fill()
    forward(int(b / 1.41))
    goto(e)
    goto(d)
    end_fill()
    forward(int(b / 1.41))

def jasny_duzy(b):
    kolor = 'light sky blue'
    fillcolor(kolor)
    begin_fill()
    forward(b)
    forward(b)
    right(135)
    forward(int(b / 1.41))
    forward(int(b / 1.41))
    right(90)
    forward(int(b / 1.41))
    forward(int(b / 1.41))
    right(135)
    forward(b)
    forward(b)
    end_fill()

def ciemny_duzy(b):
    kolor = 'royal blue'
    fillcolor(kolor)
    begin_fill()
    forward(b)
    a = pos()
    forward(b)
    right(135)
    forward(int(b / 1.41))
    c = pos()
    forward(int(b / 1.41))
    right(90)
    forward(int(b / 1.41))
    d = pos()
    forward(int(b / 1.41))
    right(135)
    forward(b)
    end_fill()

    kolor = 'light sky blue'
    fillcolor(kolor)
    begin_fill()
    goto(a)
    goto(c)
    goto(d)
    goto(a)
    end_fill()
    forward(b)









def caly(b):
    lista = []
    print(lewy_jasny(b,lista))
    print(prawy_jasny(b))
    right(90)
    print(lewy_ciemny(b, lista))
    print(prawy_ciemny(b))
    right(90)
    print(lewy_jasny(b, lista))
    print(prawy_jasny(b))
    right(90)
    print(lewy_ciemny(b, lista))
    print(prawy_ciemny(b))
    right(135)
    forward(b//2)
    left(45)
    print(ciemny_duzy(b))
    right(90)
    print(jasny_duzy(b))
    right(90)
    print(ciemny_duzy(b))
    right(90)
    print(jasny_duzy(b))
    left(45)
    forward(b//2)
    right(135)
    forward(81)
    right(90)
    forward(81)
    print(lewy_jasny(b, lista))
    print(prawy_jasny(b))
    right(90)
    print(lewy_ciemny(b, lista))
    print(prawy_ciemny(b))
    right(90)
    print(lewy_jasny(b, lista))
    print(prawy_jasny(b))
    right(90)
    print(lewy_ciemny(b, lista))
    print(prawy_ciemny(b))
    right(135)
    forward(b // 2)
    left(45)
    print(ciemny_duzy(b))
    right(90)
    print(jasny_duzy(b))
    right(90)
    print(ciemny_duzy(b))
    right(90)
    print(jasny_duzy(b))






speed(0)
print(caly(b))
exitonclick()