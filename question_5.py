from turtle import *


# Function to draw a polygon

def draw_n_gon(sides, side_length):
    for counter in range(sides):
        fd(side_length)
        lt(float(360/sides))
    
# Add your code here


# place the turtle on the left hand side of your canvas
penup()
setpos(-300,0)
pendown()

# set the pen width
pensize(2)

# set the pen colour to a green colour
pencolor("DarkOliveGreen4")

# Draw triangle
draw_n_gon(3, 50)

penup()
setpos(-200,0)
pendown()

draw_n_gon(4, 50)

penup()
setpos(-100,0)
pendown()

draw_n_gon(5, 50)

penup()
setpos(0,0)
pendown()

draw_n_gon(6, 50)

penup()
setpos(150,0)
pendown()

draw_n_gon(8, 50)

# leave the turtle on the screen until the user clicks in the screen
exitonclick()