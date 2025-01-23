from turtle import *


# place the turtle on the left hand side of your canvas
penup()
setpos(-300, 0)
pendown()

# set the pen width
pensize(2)

# set the pen colour to a green colour
pencolor("DarkOliveGreen4")

# Draw the smallest square

for counter in range(4):   # repeat 4 times
    forward(50)
    left(90)

penup()
setpos(-200, 0)
pendown()

pencolor("blue")

for counter in range(4):   # repeat 4 times
    forward(75)
    left(90)

penup()
setpos(-100, 0)
pendown()

pencolor("DarkOliveGreen4")

for counter in range(4):   # repeat 4 times
    forward(100)
    left(90)

penup()
setpos(50, 0)
pendown()

pencolor("red")

for counter in range(4):   # repeat 4 times
    forward(125)
    left(90)

# leave the turtle on the screen until the user clicks in the screen
exitonclick()
