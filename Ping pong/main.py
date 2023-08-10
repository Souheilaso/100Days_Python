from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

# paddle = Turtle("square")
# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.color("white")
# paddle.penup()
# paddle.goto(x=350, y=0)
# screen.listen()
#
#
# def go_up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)
#
#
# def go_down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)
screen.listen()
r_paddle = Paddle(350, 0)
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

l_paddle = Paddle(-350, 0)
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
