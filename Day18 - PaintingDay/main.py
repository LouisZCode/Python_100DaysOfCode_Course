import random

"""Needed to update my Python version for this exercise! Hope all good in this laptop"""

import turtle as t

t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    final_color = (r,g,b)
    return final_color

go_on = True
turtle = t.Turtle()
turtle.shape('turtle')
turtle.color('Tomato')
turtle.speed(0)


""" # A SQUARE:
for _ in range(4):
    turtle.fd(100)
    turtle.rt(90)"""

"""# DOTTED LINE
for _ in range(10):
    turtle.fd(10)
    turtle.pu()
    turtle.fd(10)
    turtle.pd()"""

""" # INCREASING ANGLE FORMS
turtle.pu()
turtle.setpos(-70.00,300.00)
turtle.pd()

n = 1
ds = 360 / n

for _ in range (100):
    n += 1
    turtle.color(random.choice(color))
    for _ in range(n):
        ds = 360 / n
        turtle.fd(100)
        turtle.rt(ds)
"""

"""# A RANDOM WALK
turtle.width(15)
directions = [0, 90, 180, 270]


while go_on:
    turtle.seth(random.choice(directions))
    turtle.forward(30)
    turtle.color(random_color())"""

""" #Magic Circles
while go_on:
    turtle.circle(100)
    turtle.right(5)
    turtle.color(random_color())"""


total = 500

print(.2 * total)


my_screen = t.Screen()
my_screen.exitonclick()