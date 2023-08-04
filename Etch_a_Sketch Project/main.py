from turtle import Turtle, Screen

tim = Turtle()


def forward():
    tim.forward(20)


def backward():
    tim.backward(20)


def left():
    tim.left(90)


def right():
    tim.right(90)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=left)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
