from turtle import *

goto(0 , 0)
def trojkat(d):
    forward(d)
    right(30)
    forward(d)
    right(120)
    forward(d)
    right(120)
    forward(d)
    right(120)

def trojkat2(d):
    forward(d)
    left(120)
    forward(d)
    left(120)
    forward(d)
    left(120)

def sierodek(d):
    for i in range(0,6):
        forward(d)
        left(30)
        forward(d)
        left(150)
        forward(d)
        left(30)
        forward(d)
        left(180)
        forward(d)
        left(30)
        forward(d)
        left(150)
        forward(d)
        left(30)
        forward(d)
        left(180)

def czerwone(d):
    forward(d)
    left(30)
    forward(d)
    right(120)
    begin_fill()
    for i in range(0,12):
        kolor = '#FF4F47'
        fillcolor(kolor)
        begin_fill()
        print(trojkat(d))
        end_fill()

def zielone(d):
    for i in range(0,12):
        kolor = '#808000'
        fillcolor(kolor)
        begin_fill()
        forward(50)
        right(30)
        print(trojkat2(d))
        end_fill()

def romb(d):
    left(60)
    forward(d)
    kolor = '#FFA500'
    fillcolor(kolor)
    begin_fill()
    for i in range(0,12):
        kolor = '#FFA500'
        fillcolor(kolor)
        right(30)
        forward(d)
        left(120)
        forward(d)
        left(60)
        forward(d)
        left(120)
        forward(d)
        end_fill()
        left(120)
        forward(d)
        right(180)
        forward(d)
        left(30)
        forward(d)
        left(90)
        forward(d)
        begin_fill()

def rozeta(w):
    print(sierodek(w))
    print(czerwone(w))
    print(zielone(w))
    print(romb(w))

speed(0)
print(rozeta(50))
exitonclick()