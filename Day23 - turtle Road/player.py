STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.goto(0,-280)
        self.setheading(90)

    def player_move(self):
        self.forward(MOVE_DISTANCE)

    def player_restart(self):
        self.teleport(x=0, y=-280)

