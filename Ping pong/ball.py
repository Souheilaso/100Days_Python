from turtle import Turtle
XMOVE = 10
YMOVE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(x=0, y=0)

    def move(self):
        new_x = self.xcor() + XMOVE
        new_y = self.ycor() + YMOVE
        self.goto(new_x, new_y)
