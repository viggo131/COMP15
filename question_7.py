from turtle import *

# produce pattern rotation

'''
# using for loop
def draw_spiral(sides, initial_length, decrement):
    length = initial_length
    for counter in range(20):
        fd(length)
        lt(float(360/sides))
        length -= decrement
'''

# using while loop
def draw_spiral(sides, initial_length, decrement):
    length = initial_length
    while length > 0:
        fd(length)
        lt(float(360/sides))
        length -= decrement

# set the pen width and speed
pensize(2)
speed(100)

# pos 1
penup()
setpos(-400,0)
setheading(0)
pendown()

draw_spiral(3, 100, 5)

# pos 2
penup()
setpos(-200,0)
setheading(0)
pendown()

draw_spiral(4, 100, 5)

# pos 3
penup()
setpos(0,0)
setheading(0)
pendown()

draw_spiral(5, 100, 5)

# pos 4
penup()
setpos(200,0)
setheading(0)
pendown()

draw_spiral(6, 100, 4)

# pos 5
penup()
setpos(400,0)
setheading(0)
pendown()

draw_spiral(8, 75, 2)

exitonclick()