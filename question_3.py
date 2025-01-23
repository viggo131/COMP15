from turtle import *


# Function to draw a square

def draw_square(side_length):
    
    for counter in range(4):
        fd(side_length)
        lt(90)


# place the turtle on the left hand side of your canvas
penup()
setpos(-225, 0)
pendown()

# set the pen width
pensize(2)

# set the pen colour to a green colour
pencolor("DarkOliveGreen4")

# Draw square
draw_square(50)

#draw square 2
penup()
goto(-100,0)
pendown()

pencolor("blue")

draw_square(75)

#draw square 3
penup()
goto(0,0)
pendown()

pencolor("red")

draw_square(100)

#draw square 4
penup()
goto(125,0)
pendown()

pencolor("green")

draw_square(125)


# leave the turtle on the screen until the user clicks in the screen
exitonclick()
