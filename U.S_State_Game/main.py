import turtle

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# get x and y coordinate


def get_mouse_click(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click)
answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?")
# using this instead of screen.exitonclick
turtle.mainloop()


