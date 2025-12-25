from turtle import *
def kwadracik(bok,kolor):
    pd()
    fillcolor(kolor)
    begin_fill()
    for i in range(0,4):
        forward(bok)
        left(90)
    forward(bok)
    end_fill()
    pu()

def pientro(ileP,ileL):
    c = 0
    for i in range(0,ileL):
        if i<6:
            kwadracik(100,'orange')
        else:
            kwadracik(100,'yellow')
        c = i

    zero = pos()
    goto(zero[0]+300,zero[1])
    for j in range(0,ileP):
        if c+j<6:
            kwadracik(100,'orange')
        else:
            kwadracik(100,'yellow')


def obramowka(bok,kolor):
    for i in range(0,28):
        kwadracik(bok,kolor)
    left(90)
    for i in range(0,22):
        kwadracik(bok,kolor)
    left(90)
    for i in range(0, 28):
        kwadracik(bok, kolor)
    left(90)
    for i in range(0, 22):
        kwadracik(bok, kolor)
    left(90)

def pasek(bok,kolor):
    pd()
    fillcolor(kolor)
    begin_fill()
    forward(1300)
    right(90)
    forward(10)
    right(90)
    forward(1300)
    right(90)
    forward(10)
    right(90)
    end_fill()
    pu()



def liczydlo():
    bok = 50
    n = 9000708
    c = 0
    lista = [0]*7
    while n>0 and c<7:
        lista[c] = n%10
        n = n//10
        c = c+1

    print(lista)



    obramowka(bok,'black')
    goto(-650, 455)
    zero = pos()
    for i in range(0,7):
     pasek(10,'black')
     goto(zero[0], zero[1]-150)
     zero = pos()




    goto(-650, -500)
    zero = pos()
    for i in lista:
        L = i
        P = 10-i
        pientro(P,L)
        goto(zero[0], zero[1]+150)
        zero = pos()
pu()
goto(-700,-550)
speed(0)
liczydlo()
exitonclick()
