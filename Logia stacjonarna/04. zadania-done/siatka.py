from turtle import*

def pros(bok,kolor):
    pd()
    fillcolor(kolor)
    begin_fill()
    forward(bok)
    left(90)
    forward(bok*2)
    left(90)
    forward(bok)
    left(90)
    forward(bok * 2)
    left(90)
    forward(bok)
    end_fill()
    pu()
def szes(bok):
    pd()
    fillcolor('purple')
    begin_fill()
    forward(bok)
    right(60)
    forward(bok)
    right(60)
    forward(bok)
    right(60)
    forward(bok)
    right(60)
    forward(bok)
    right(60)
    forward(bok)
    right(60)

    end_fill()
    pu()


def siatka():
    szes(70)
    for i in range(0,6):
        if i%2==0:
            pros(70,'blue')
            right(60)
        else:
            pros(70, 'orange')
            right(60)


siatka()
exitonclick()