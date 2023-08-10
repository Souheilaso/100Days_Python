from turtle import Turtle


class Paddle:
    def __init__(self, x, y):
        self.paddle = Turtle("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.goto(x, y)

    def go_up(self):
        new_y = self.paddle.ycor() + 20
        self.paddle.sety(new_y)

    def go_down(self):
        new_y = self.paddle.ycor() - 20
        self.paddle.sety(new_y)
