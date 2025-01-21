from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.total_score = 0
        self.speed(0)
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(-20, 260)
        self.write(f"SCORE: {self.total_score}", False, "center", font=('Arial', 24, 'normal'))

    def point(self):
        self.clear()
        self.total_score += 1
        self.write(f"SCORE: {self.total_score}", False, "center", font=('Arial', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, "center", font=('Arial', 24, 'normal'))
