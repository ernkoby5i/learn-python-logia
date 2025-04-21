from random import randint
from turtle import *

colormode(255)
tracer(0)  # lepiej nie stosować na konkursach (chyba, że do testów)


def gwiazdka():
    rozmiar = randint(5, 25)
    kat = randint(120, 180)
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    pencolor(r, g, b)
    for i in range(randint(10, 50)):
        fd(rozmiar)
        rt(kat)
    penup()
    fd(randint(5, 30))
    pendown()


for i in range(5000):
    gwiazdka()
    if i % 100 == 0:
        teleport(0, 0)

update()

mainloop()
