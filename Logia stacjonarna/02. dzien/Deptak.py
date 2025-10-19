from turtle import *

def trojkat(bok, kolor):
    fillcolor(kolor)
    begin_fill()
    pd()
    zero = pos()
    goto(zero[0] -bok//2,zero[1] -bok//2)
    goto(zero[0] + bok//2,zero[1]-bok//2)
    goto(zero)
    end_fill()
    pu()

def caly():
    zero = pos()
    bok = 100
    trojkat(bok,'light sky blue')
    trojkat(bok / 3, 'royal blue')
    goto(zero[0] - bok // 6, zero[1] - bok // 6)
    trojkat(bok / 3, 'royal blue')
    goto(zero[0] + bok // 6, zero[1] - bok // 6)
    trojkat(bok / 3, 'royal blue')
    goto(zero[0] + bok // 6, zero[1] - bok // 6)
    akt = pos()
    goto(akt[0] - bok // 6, akt[1] - bok // 6)
    trojkat(bok / 3, 'royal blue')
    goto(zero)

def trujat2(bok,kolor):
    fillcolor(kolor)
    begin_fill()
    pd()
    zero = pos()
    goto(zero[0] +bok//2,zero[1] +bok//2)
    goto(zero[0] + bok//2,zero[1]-bok//2)
    goto(zero)
    end_fill()
    pu()

def prawycaly():
    zero = pos()
    bok = 100
    trujat2(bok,'royal blue')
    trujat2((bok/3)*2, 'light sky blue')
    goto(zero[0] + (bok/3),zero[1])
    trujat2((bok / 3), 'light sky blue')
    goto(zero)

def trujat3(bok, kolor):
    fillcolor(kolor)
    begin_fill()
    pd()
    zero = pos()
    goto(zero[0] - bok // 2, zero[1] - bok // 2)
    goto(zero[0] - bok // 2, zero[1] + bok // 2)
    goto(zero)
    end_fill()
    pu()

def lewycaly():
    zero = pos()
    bok = 100
    trujat3(bok, 'royal blue')
    trujat3((bok / 3) * 2, 'light sky blue')
    goto(zero[0] - (bok / 3), zero[1])
    trujat3((bok / 3), 'light sky blue')
    goto(zero)

def trojkat4(bok, kolor):
    fillcolor(kolor)
    begin_fill()
    pd()
    zero = pos()
    goto(zero[0] - bok // 2, zero[1] + bok // 2)
    goto(zero[0] + bok // 2, zero[1] + bok // 2)
    goto(zero)
    end_fill()
    pu()

def gora():
    zero = pos()
    bok = 100
    trojkat4(bok, 'light sky blue')
    trojkat4(bok / 3, 'royal blue')
    goto(zero[0] - bok // 6, zero[1] + bok // 6)
    trojkat4(bok / 3, 'royal blue')
    goto(zero[0] + bok // 6, zero[1] + bok // 6)
    trojkat4(bok / 3, 'royal blue')
    goto(zero[0], zero[1] + bok // 3)
    trojkat4(bok / 3, 'royal blue')
    pu()
    goto(zero[0], zero[1] - bok)

def trojkat5(bok, kolor):
    fillcolor(kolor)
    begin_fill()
    pd()
    zero = pos()
    goto(zero[0] + bok // 2, zero[1] + bok // 2)
    goto(zero[0] + bok // 2, zero[1] - bok // 2)
    goto(zero)
    end_fill()
    pu()

def prawy2():
    zero = pos()
    bok = 100
    trojkat5(bok, 'light sky blue')
    trojkat5(bok / 3, 'royal blue')
    goto(zero[0] + bok // 6, zero[1] - bok // 6)
    trojkat5(bok / 3, 'royal blue')
    goto(zero[0] + bok // 6, zero[1] + bok // 6)
    trojkat5(bok / 3, 'royal blue')
    goto(zero[0] + bok // 3, zero[1])
    trojkat5(bok / 3, 'royal blue')
    pu()
    goto(zero)

def trojkat6(bok, kolor):
    fillcolor(kolor)
    begin_fill()
    pd()
    zero = pos()
    goto(zero[0] - bok // 2, zero[1] - bok // 2)
    goto(zero[0] - bok // 2, zero[1] + bok // 2)
    goto(zero)
    end_fill()
    pu()

def lewy2():
    zero = pos()
    bok = 100
    trojkat6(bok, 'light sky blue')
    trojkat6(bok / 3, 'royal blue')
    goto(zero[0] - bok // 6, zero[1] + bok // 6)
    trojkat6(bok / 3, 'royal blue')
    goto(zero[0] - bok // 6, zero[1] - bok // 6)
    trojkat6(bok / 3, 'royal blue')
    goto(zero[0] - bok // 3, zero[1])
    trojkat6(bok / 3, 'royal blue')
    pu()
    goto(zero)


def trujat7(bok,kolor):
    fillcolor(kolor)
    begin_fill()
    pd()
    zero = pos()
    goto(zero[0] -bok//2,zero[1] +bok//2)
    goto(zero[0] + bok//2,zero[1]+bok//2)
    goto(zero)
    end_fill()
    pu()

def gora2():
    zero = pos()
    bok = 100
    trujat7(bok,'royal blue')
    trujat7((bok/3)*2, 'light sky blue')
    goto(zero[0],zero[1] + (bok/3))
    trujat7((bok / 3), 'light sky blue')
    goto(zero)

def trujat8(bok,kolor):
    fillcolor(kolor)
    begin_fill()
    pd()
    zero = pos()
    goto(zero[0] +bok//2,zero[1] -bok//2)
    goto(zero[0] - bok//2,zero[1]-bok//2)
    goto(zero)
    end_fill()
    pu()

def dol2():
    zero = pos()
    bok = 100
    trujat8(bok,'royal blue')
    trujat8((bok/3)*2, 'light sky blue')
    goto(zero[0],zero[1] - (bok/3))
    trujat8((bok / 3), 'light sky blue')
    goto(zero)
    goto(zero[0] + (bok), zero[1] + (bok))


if __name__ == "__main__":
    n = int(input())
    bok = 100
    pu()
    goto(-(bok*(n/2))/2, bok/2)
    pd()
    for i in range(0,n*2):
        caly()
        prawycaly()
        lewycaly()
        gora()
        prawy2()
        lewy2()
        dol2()
        gora2()


    exitonclick()