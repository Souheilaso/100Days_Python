import tkinter

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

# Create a window
window = tkinter.Tk()
# Window title
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)

# Creating canvas
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Finding the image using PhotoImage
image = tkinter.PhotoImage(file="tomato.png")
# Creating the image
canvas.create_image(100, 112, image=image)
# Adding timing text
canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
# Layout
canvas.grid(column=1, row=1)  # Use grid instead of pack

# Creating Timer label
timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# Keep the window open
window.mainloop()

