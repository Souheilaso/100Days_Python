import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_rgb = (r, g, b)
    return color_rgb


directions = [0, 90, 180, 270]
tim.width(10)
for _ in range(200):
    tim.color(random_color())
    tim.speed('fastest')
    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = Screen()
screen.exitonclick()
