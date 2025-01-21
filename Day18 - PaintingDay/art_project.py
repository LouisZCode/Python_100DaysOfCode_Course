#import cologram
import turtle as t

"""
The laptop does not let me import packages, I imagine because of permits
So I will use replit.com for this one sadly...
"""

"""Even so, the final projects looks like this:"""

import turtle as t
import random
t.colormode(255)

go_on = True
turtle = t.Turtle()
turtle.shape('turtle')
turtle.color('Tomato')
turtle.speed(5)
turtle.hideturtle()

rgb_colors = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


turtle.pu()
turtle.setpos(-120.00,-100)
turtle.width(20)


def line_of_dots(number):
    for _ in range(number):
        #to make a DOT
        turtle.color(random.choice(rgb_colors))
        turtle.pd()
        turtle.forward(1)
        turtle.pu()
        turtle.forward(20)

def jump_to_next_line(number):
    #jumps to the next line
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(21*number)
    turtle.left(180)

number = 10

for _ in range(number):
    line_of_dots(number)
    jump_to_next_line(number)


my_screen = t.Screen()
my_screen.exitonclick()