#https://logia.oeiizk.waw.pl/strony/archiwalne/L25_zadania_e2.pdf
from turtle import *
def schodekL(bok):
    pd()
    left(90)
    forward(bok)
    right(90)
    forward(bok)
    pu()






def schodekP(bok):
    pd()
    forward(bok)
    left(90)
    forward(bok)
    right(90)
    pu()



def caly():
    n = '124456789'
    lista = [int(c) for c in n]
    print(lista)

    P = []
    N = []
    for i in lista:
        if i%2==0:
            P.append(i)
        else:
            N.append(i)
    print(len(P))
    bok = 300/(len(P)+1)
    for i in range(0,len(P)):
        schodekL(bok)
    pd()
    goto(0,150)
    pu()


    goto(0,-150)
    pd()
    goto(300, -150)
    pu()
    left(90)

    print(len(N))
    bok = 300 / (len(N) + 1)
    for i in range(0,len(N)):
        schodekP(bok)
    pd()
    goto(0, 150)
    pu()


pu()
goto(0,-150)
pd()
goto(-300,-150)
pu()
speed(0)
caly()
exitonclick()

