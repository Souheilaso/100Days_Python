from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 70, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 200)
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def points(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)