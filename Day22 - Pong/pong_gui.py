from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.ht()
        self.pu()
        self.l_score = 0
        self.r_score = 0


    def create_line(self):
        self.color("white")
        self.ht()
        self.pu()
        self.goto(0, 300)
        self.right(90)
        for _ in range(30):
            self.pd()
            self.forward(10)
            self.penup()
            self.forward(10)

    def upate_score(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=("courier", 60, "normal"))
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=("courier", 60, "normal"))

    def score_r(self):
        self.r_score += 1
        self.upate_score()

    def score_l(self):
        self.l_score += 1
        self.upate_score()

