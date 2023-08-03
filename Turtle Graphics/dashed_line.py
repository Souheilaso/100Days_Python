from turtle import *

tim = Turtle()
shape = tim.shape("classic")

for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


# screen is to show a screen with the design
screen = Screen()
# The moment we click on the screen it exists
screen.exitonclick()
