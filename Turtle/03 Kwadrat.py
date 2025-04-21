from turtle import *
l = ["yellow","green","blue","red"]


for c in range(0,2):
    pencolor(l[c])
    for i in range(25):
        forward(50)
        left(90)
        forward(1)
        left(90)
        forward(50)
        right(90)
        forward(1)
        right(90)


pencolor("black")
left(270)
forward(100)
right(90)



for c in range(2,4):
    pencolor(l[c])
    for i in range(25):
        forward(50)
        right(90)
        forward(1)
        right(90)
        forward(50)
        left(90)
        forward(1)
        left(90)

pencolor("black")
left(90)
forward(100)
left(90)
forward(50)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(180)
forward(100)












#fd(50)
#lt(90)

#fd(50)
#lt(90)

#fd(50)
#lt(90)


done()