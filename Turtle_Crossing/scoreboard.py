from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Courier", 20, "normal")
FONT2 = ("Courier", 70, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-280, 260)
        self.write("Score: " + str(self.score), align=ALIGNMENT, font=FONT)

    def points(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT2)
