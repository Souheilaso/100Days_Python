from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

screen.listen()
r_paddle = Paddle(350, 0)
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

l_paddle = Paddle(-350, 0)
screen.onkey(l_paddle.go_up, "s")
screen.onkey(l_paddle.go_down, "c")

ball = Ball()
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    screen.update()

screen.exitonclick()
