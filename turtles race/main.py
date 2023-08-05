import turtle
from turtle import Turtle, Screen
import random

colors = ["red", "orange", "pink", "green", "blue", "purple"]
random.shuffle(colors)  # Shuffle the colors list to distribute colors more evenly

is_race_on = False
all_turtles = []


def race_turtle(name, x, y, color):
    name_instance = Turtle("turtle")
    name_instance.color(color)
    name_instance.penup()
    name_instance.goto(x=x, y=y)
    name_instance.name = name  # Set the name of the turtle
    all_turtles.append(name_instance)
    return name_instance


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?"
                                                          " (red, orange, pink, green, blue, purple)Enter a color: ")
# creating turtles
t1 = race_turtle("tim", x=-241, y=-1, color=colors[0])
t2 = race_turtle("sara", x=-241, y=-30, color=colors[1])
t3 = race_turtle("adao", x=-241, y=30, color=colors[2])
t4 = race_turtle("jade", x=-241, y=-60, color=colors[3])
t5 = race_turtle("lava", x=-241, y=-90, color=colors[4])
t6 = race_turtle("purl", x=-241, y=60, color=colors[5])
turtle.hideturtle()

if user_bet:
    is_race_on = True

# Set the turtle speed to maximum for a faster race
turtle.speed("fastest")

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
        if turtle.xcor() > 241:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You win!")
            else:
                print(f"You have lost. {winning_color} is the winner turtle")
            break
    screen.update()  # Update the screen after each move

# Keep the window open until clicked
screen.exitonclick()
