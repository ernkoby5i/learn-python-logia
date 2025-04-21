import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle
pen = turtle.Turtle()
pen.speed(5)
pen.pensize(2)

def draw_colored_square(x, y, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(100)
        pen.right(90)
    pen.end_fill()

# Coordinates for each square (2x2 grid)
start_x = -100
start_y = 100
offset = 110

# Draw the squares like the Windows logo
draw_colored_square(start_x, start_y, "blue")          # Top-left
draw_colored_square(start_x + offset, start_y, "red")  # Top-right
draw_colored_square(start_x, start_y - offset, "green")# Bottom-left
draw_colored_square(start_x + offset, start_y - offset, "yellow") # Bottom-right

pen.hideturtle()
screen.mainloop()
