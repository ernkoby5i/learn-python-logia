from turtle import *
def kwadrat(bok,kolor):
    pd()
    fillcolor(kolor)
    begin_fill()
    for i in range(0,4):
        forward(bok)
        left(90)
    end_fill()
    pu()


def wie():

    n =''
    Licznik_B = 1
    for i in range(1,len(n)):
        if n[i]!=n[i-1]:
            Licznik_B = Licznik_B+1
    print(Licznik_B)

    Licznik_P = 1
    licznik = 1
    for i in range(1,len(n)):
        if n[i]==n[i-1]:

            licznik = licznik+1
            if licznik>Licznik_P:
                Licznik_P = licznik
        else:
            licznik = 1
    print(Licznik_P)

    if Licznik_P>Licznik_B:
        c = Licznik_P
    else:
        c = Licznik_B


    bok = 400/c
    goto(-bok*Licznik_B,0)
    P = n[0]
    for i in range(len(n)):
        if P!=n[i]:
            zero = pos()
            goto(zero[0]+bok,0)
        if n[i]=='G':
            kwadrat(bok,'olive')
            left(90)
            forward(bok)
            right(90)
            P = n[i]
        else:
            kwadrat(bok, 'gold')
            left(90)
            forward(bok)
            right(90)
            P = n[i]

pu()
speed(0)
wie()
exitonclick()
