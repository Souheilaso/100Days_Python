from turtle import *

tim = Turtle()
shape = tim.shape("turtle")


def square():
    for _ in range(4):
        tim.forward(100)
        tim.left(90)


square()
# screen is to show a screen with the design
screen = Screen()
# The moment we click on the screen it exists
screen.exitonclick()
