from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


# def snakes(x, y):
#     snake = Turtle("square")
#     snake.color("white")
#     snake.goto(x, y)
#     return snake
#
#
# snake1 = snakes(0, 0)
# snake2 = snakes(-20, 0)
# snake3 = snakes(-40, 0)

snake_position = [(0, 0), (-20, 0), (-40, 0)]
for position in snake_position:
    snake = Turtle("square")
    snake.color("white")
    snake.goto(position)

screen.exitonclick()
