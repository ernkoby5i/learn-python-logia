import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(5)
pen.pensize(2)

def draw_tilted_square(x, y, size, color, angle):
    pen.penup()
    pen.goto(x, y)
    pen.setheading(angle)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(size)
        pen.right(90)
    pen.end_fill()

# Function to calculate tilted positions
def tilted_position(x, y, angle_deg, distance):
    angle_rad = math.radians(angle_deg)
    dx = math.cos(angle_rad) * distance
    dy = math.sin(angle_rad) * distance
    return x + dx, y - dy

# Base position and settings
base_x = -100
base_y = 100
size = 100
angle = 15
gap = 10

# Draw the 4 tilted squares
# Top-left (Blue)
draw_tilted_square(base_x, base_y, size, "blue", angle)

# Top-right (Red)
x2, y2 = tilted_position(base_x, base_y, angle, size + gap)
draw_tilted_square(x2, y2, size, "red", angle)

# Bottom-left (Green)
x3, y3 = tilted_position(base_x, base_y, angle + 90, size + gap)
draw_tilted_square(x3, y3, size, "green", angle)

# Bottom-right (Yellow)
x4, y4 = tilted_position(x2, y2, angle + 90, size + gap)
draw_tilted_square(x4, y4, size, "yellow", angle)

pen.hideturtle()
screen.mainloop()
