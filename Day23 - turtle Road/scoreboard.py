from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.goto(-280, 250)
        self.score = 0
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(arg=f"Level:{self.score}", font=FONT)

