from turtle import *



def Motyw():
    w = 60
    speed(0)
    penup()
    goto(90, -90)
    s = pos()
    left(150)
    for i in range(0,4):
        right(60)
        pozycje = []
        print(szesc(w,pozycje))
        print(maly(w,pozycje))

        forward(30)
        left(60)
        if (i!=3):
            forward(w)
    penup()
    goto(s)
    left(60)
    forward(60)
    right(60)
    forward(60)
    pendown()
    for i in range(0,3):
        right(60)
        pozycje = []
        print(szesc(w,pozycje))
        print(maly(w,pozycje))

        forward(30)
        left(60)
        if (i!=2):
            forward(w)
    penup()
    goto(s)
    left(60)
    forward(60)
    left(60)
    forward(60)
    right(60)
    forward(60)
    right(60)
    forward(60)
    pendown()

    for i in range(0,4):
        right(60)
        pozycje = []
        print(szesc(w,pozycje))
        print(maly(w,pozycje))

        forward(30)
        left(60)
        if (i!=3):
            forward(w)
    penup()
    goto(s)
    right(60)
    forward(60)
    right(60)
    forward(60)
    left(60)
    forward(60)
    left(60)
    forward(60)
    right(60)
    forward(60)
    pendown()
    for i in range(0,1):
        right(60)
        pozycje = []
        print(szesc(w,pozycje))
        print(maly(w,pozycje))

    penup()
    goto(s)
    left(180)
    forward(60)
    right(60)
    forward(60)
    left(60)
    forward(60)
    right(60)
    forward(60)
    left(60)
    forward(60)
    right(60)
    forward(60)
    right(60)
    forward(60)
    pendown()
    for i in range(0,1):
        right(60)
        pozycje = []
        print(szesc(w,pozycje))
        print(maly(w,pozycje))









def szesc(d,pozycje):
    pd()
    kolor = 'gold'
    fillcolor(kolor)
    begin_fill()
    for i in range(0,6):
        forward(30)
        x = pos()
        pozycje.append(x)
        forward(30)
        right(60)
    end_fill()
    forward(30)
    pu()

def maly(d,pozycje):
    pd()
    end_fill()
    goto(pozycje[0])
    kolor = 'dark orange'
    fillcolor(kolor)
    begin_fill()
    goto(pozycje[1])
    goto(pozycje[2])
    goto(pozycje[3])
    goto(pozycje[4])
    goto(pozycje[5])
    goto(pozycje[0])
    end_fill()
    pu()

if __name__ == "__main__":
    Motyw()




