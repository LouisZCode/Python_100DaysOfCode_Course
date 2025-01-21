from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setpos(new_x, new_y)

    def ball_accelerate(self):
        self.x_move += 5
        self.y_move += 5

    def ball_reset(self):
        self.setpos(0, 0)
        self.ball_move()
        self.move_speed = 0.1

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= .7

    def score_right(self):
        if self.xcor() > 380:
            return 1

    def score_left(self):
        if self.xcor() < -380:
            return 1


