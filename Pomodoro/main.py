# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
import tkinter

# create a window
window = tkinter.Tk()
# Window title
window.title("POMODORO")

# creating canvas
canvas = tkinter.Canvas(width=200, height=224)
# finding the image using photoimage
image = tkinter.PhotoImage(file="tomato.png")
# creating the image
canvas.create_image(100, 112, image=image)

# Keep the window open
window.mainloop()
