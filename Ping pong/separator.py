from turtle import Turtle


class Separator(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, -300)

    def draw(self):
        self.setheading(90)
        for _ in range(30):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)