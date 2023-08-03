from turtle import Turtle, shape, Screen
import random
tim = Turtle()
shape = shape("classic")
colors = ["medium violet red", "purple", "dark magenta", "violet", "magenta", "thistle", "plum",
          "orchid", "medium orchid", "dark orchid"]


def draw_shape(num_sides):
    angel = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angel)


for shapes in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shapes)


screen = Screen()
screen.exitonclick()
