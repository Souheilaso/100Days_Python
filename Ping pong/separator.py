from turtle import Turtle


class Separator(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, -300)
        self.pendown()
        self.goto(0, 300)