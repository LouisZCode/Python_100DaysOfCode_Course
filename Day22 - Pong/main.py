from turtle import Screen, Turtle
import time
from paddle import Paddle
from pong_gui import Score
from ball import Ball


# Game screen setup
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My PONG Game")
screen.tracer(0)


#Create line func from gui
middle_line = Score()
middle_line.create_line()


#Score setup from gui (pending)
score = Score()

# Paddle setup
paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))


# Paddle movement controls
screen.listen()
screen.onkey(paddle.up, "Up")
screen.onkey(paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


#Ball setup:
ball = Ball()


# Game loop
game_on = True
while game_on:
    score.upate_score()
    time.sleep(ball.move_speed)  # Add a delay to reduce CPU usage
    screen.update()  # Update the screen after each frame
    ball.ball_move()

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    if (ball.distance(paddle) < 50 and ball.xcor() > 320 or
        ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.score_right():
        score.score_l()
        ball.ball_reset()
        ball.bounce_x()

    if ball.score_left():
        score.score_r()
        ball.ball_reset()
        ball.bounce_x()



screen.exitonclick()
