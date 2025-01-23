from turtle import *


# Function to draw a square

def draw_square(side_length):
    
    for counter in range(4):
        fd(side_length)
        lt(90)

def draw_triagle(side_length):
    
    for counter in range(3):
        fd(side_length)
        lt(120)

def draw_pentagon(side_length):
    
    for counter in range(5):
        fd(side_length)
        lt(72)

def draw_hexagon(side_length):
    
    for counter in range(6):
        fd(side_length)
        lt(60)

def draw_octagon(side_length):
    
    for counter in range(8):
        fd(side_length)
        lt(45)

# place the turtle on the left hand side of your canvas
penup()
setpos(-300, 0)
pendown()

# set the pen width
pensize(2)

# set the pen colour to a green colour
pencolor("DarkOliveGreen4")

# Draw square
draw_triagle(50)

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

penup()
goto(-100,0)
pendown()

draw_pentagon(75)

penup()
goto(100,0)
pendown()

draw_hexagon(100)

# draw octogon

penup()
goto(350,0)
pendown()

draw_octagon(100)






# leave the turtle on the screen until the user clicks in the screen
exitonclick()
