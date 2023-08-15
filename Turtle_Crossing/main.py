from turtle import Screen
from car_manager import CarManager
import random
import time
from player import Player
from scoreboard import Score
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Racing")
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")
cars = []
score = Score()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if random.randint(1, 6) == 1:
        new_car = CarManager()
        cars.append(new_car)
    for car in cars:
        car.move()
# cars collision with turtle
    for car in cars:
        if car.distance(player) < 20:  # Adjust the distance as needed
            game_is_on = False
# turtle collision with wall
    if player.ycor() > 280:
        score.points()
        score.update_score()
        game_is_on = False

screen.exitonclick()
