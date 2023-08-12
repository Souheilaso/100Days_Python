from turtle import Screen
from car_manager import CarManager
import time
from player import Player
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Racing")
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")
car = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
screen.exitonclick()
