import turtle
import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(500, 400)

user_choice = screen.textinput("Make a bet!", "My Choice:")
y_coordinate = [70, 40, 10, -20, -50]
color = ["red", 'blue', 'yellow', 'orange', 'purple']
all_turtles = []

#I did it manually! not good. It is much better to do it like this:
for turtle_index in range(5):
    tur1 = t.Turtle(shape='turtle')
    tur1.color(color[turtle_index])
    tur1.penup()
    tur1.goto(-240, y=y_coordinate[turtle_index])
    all_turtles.append(tur1)

if user_choice:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_choice:
                print(f'winner is the {winning_turtle} turtle!')
                print("_________________YOU WON!!______________________")
            else:
                print(f'Oh no... the winner is the {winning_turtle} turtle....')
                print('_________________YOU LOST!!______________________')

        distance = random.randint(0,10)
        turtle.forward(distance)

screen.exitonclick()