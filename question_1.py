from turtle import *

# place the turtle on the left hand side of your canvas
penup()
setpos(-300, 0)
pendown()

# set the pen width
pensize(2)

# set the pen colour to a green colour
pencolor("green")

# Draw a square
forward(50)     # move forward 50 pixels
left(90)        # turn left 90 degrees
forward(50)
lt(90)          # an abbreviation for turn left
fd(50)          # an abbreviation for move forward
lt(90)
fd(50)
lt(90)

# set the pen colour to a red colour
pencolor("blue")

penup()
setpos(-200, 0)
pendown()

# Draw a 2nd square
forward(75)     # move forward 75 pixels
left(90)        # turn left 90 degrees
forward(75)
lt(90)          # an abbreviation for turn left
fd(75)          # an abbreviation for move forward
lt(90)
fd(75)
lt(90)

# set the pen colour to a green colour
pencolor("green")

penup()
setpos(-100, 0)
pendown()

# Draw a 3nd square
forward(100)     # move forward 100 pixels
left(90)        # turn left 90 degrees
forward(100)
lt(90)          # an abbreviation for turn left
fd(100)          # an abbreviation for move forward
lt(90)
fd(100)
lt(90)

# set the pen colour to a red colour
pencolor("red")

penup()
setpos(50, 0)
pendown()

# Draw a 4th square
forward(125)     # move forward 125 pixels
left(90)        # turn left 90 degrees
forward(125)
lt(90)          # an abbreviation for turn left
fd(125)          # an abbreviation for move forward
lt(90)
fd(125)
lt(90)

# leave the turtle on the screen until the user clicks in the screen
exitonclick()
