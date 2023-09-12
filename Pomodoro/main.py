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
window.config(padx=100, pady=50, bg=YELLOW)

# creating canvas
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# finding the image using photoimage
image = tkinter.PhotoImage(file="tomato.png")
# creating the image
canvas.create_image(100, 112, image=image)
# Adding timing text
canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
# layout
canvas.pack()

# Keep the window open
window.mainloop()
