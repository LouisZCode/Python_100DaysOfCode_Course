from turtle import  Screen
import time
from snake import Snake
from food import Food
from score import Score

"""Screen Settings"""
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
"""New one to make animations off"""
screen.tracer(0)   #You need the update() or nothing will happen!


""" #Tried to do a head indepentend, but better to have a full code for all pieces:
snake_head = Turtle("square")
snake_head.color("white")
position_head = snake_head.pos()
"""

"""Base or Global attributed for initial Snake"""
"""IDEA THAT DIDNT PAN OUT
n_parts = 3
location_x = 0
location_y = 0
"""


"""
We created this as a class and then made an Object, because now all the code related to the snake
is in its own file!!  
If we get an issue with the snake, we know where to search and debbug..!! makes this much cleaner and easier
"""
snake = Snake()
food = Food()
score = Score()

screen.listen() #start listening to key strokes
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()

game_is_on = True

while game_is_on:
    screen.update()  #here, so it refreshes when all the loop happened
    """Lets make everything slower so we understand what is happening"""
    time.sleep(.08)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.point()
        snake.extend()

    #Detect collision with Wall
    if (
            snake.head.xcor() > 298 or
            snake.head.xcor() < -298 or
            snake.head.ycor() > 298 or
            snake.head.ycor() < -298
    ):
        game_is_on = False
        score.game_over()

    #Detect sollision with body:
    for segment in snake.n_parts[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            score.game_over()

screen.exitonclick()

#What if I make the edges fire and they start to enclose everytime the food is eaten!