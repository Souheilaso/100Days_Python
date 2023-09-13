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
def count_down(count):
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

# Create a window
window = tkinter.Tk()
# Window title
window.title("POMODORO")
window.config(padx=100, pady=50, bg=YELLOW)
# execute a command after a time delay
count_down(5)
# Creating canvas
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# Finding the image using PhotoImage
image = tkinter.PhotoImage(file="tomato.png")
# Creating the image
canvas.create_image(100, 112, image=image)
# Adding timing text
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
# Layout
canvas.grid(column=1, row=1)  # Use grid instead of pack

# Creating Timer label
timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# creating start button
start_button = tkinter.Button(text="Start", highlightbackground=YELLOW, highlightthickness=0, bg=YELLOW)
start_button.grid(column=0, row=3)

# creating a Restart button
restart_btn = tkinter.Button(text="Restart", highlightbackground=YELLOW, highlightthickness=0, bg=YELLOW)
restart_btn.grid(column=3, row=3)

# creating a check mark label
check_label = tkinter.Label(text="✓", fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=4)

# Keep the window open
window.mainloop()
