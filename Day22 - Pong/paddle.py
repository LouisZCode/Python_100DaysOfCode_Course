from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.resizemode("user")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)  # Adjusted size
        self.goto(position)  # Position the paddle at the given coordinates

    def up(self):
        if self.ycor() < 250:  # Prevent moving out of bounds
            self.setheading(90)
            self.forward(20)

    def down(self):
        if self.ycor() > -250:  # Prevent moving out of bounds
            self.setheading(270)
            self.forward(20)
