from turtle import *

# produce pattern rotation

def draw_n_gon(sides, side_length):
    for counter in range(sides):
        fd(side_length)
        lt(float(360/sides))

# place the turtle on the left hand side of your canvas
penup()
setpos(-400,0)
pendown()

# set the pen width
pensize(2)

speed(100)

for counter in range(8):
    draw_n_gon(3, 50)
    lt(45)

penup()
setpos(-200,0)
pendown()

for counter in range(7):
    draw_n_gon(4, 50)
    lt(51.42)

penup()
setpos(0,0)
pendown()

for counter in range(10):
    draw_n_gon(5, 50)
    lt(36)

penup()
setpos(200,0)
pendown()

for counter in range(11):
    draw_n_gon(6, 50)
    lt(32.73)

penup()
setpos(500,0)
pendown()

for counter in range(12):
    draw_n_gon(8, 50)
    lt(30)

exitonclick()