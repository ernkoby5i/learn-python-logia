
from turtle import *

pencolor("red")

def wielokat(n):
    kat = (n-2)*180/n
    for i in range(n):
        fd(50)
        lt(180 - kat)

wielokat(6)

pencolor("blue")

wielokat(4)

done()