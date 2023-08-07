import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

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
# snakes = []
#
# snake_position = [(0, 0), (-20, 0), (-40, 0)]
# for position in snake_position:
#     snake = Turtle("square")
#     snake.color("white")
#     snake.penup()
#     snake.goto(position)
#     snakes.append(snake)
snake = Snake()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    # for snake_num in range(len(snakes) - 1, 0, -1):
    #     new_x = snakes[snake_num - 1].xcor()
    #     new_y = snakes[snake_num - 1].ycor()
    #     snakes[snake_num].goto(new_x, new_y)
    snake.move()

screen.exitonclick()
