from turtle import*


def zegar():
    pu()
    goto(0,-90)
    tablica = []
    tablica2 = []
    for i in range(0,12):
        circle(90,30)
        tablica.append(pos())

    goto(0, -110)
    for i in range(0,12):
        circle(110,30)
        tablica2.append(pos())

    for i in range(0,12):
        goto(tablica[i])
        pd()
        goto(tablica2[i])
        pu()



zegar()
exitonclick()