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
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:  # After 4 work intervals, take a long break
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:  # After every even work interval, take a short break
        count_down(short_break_sec)
        timer_label.config(text="Short Break", fg=PINK)
    else:  # Otherwise, work interval
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = count // 60  # Use integer division to get minutes
    count_sec = count % 60  # Use modulo to get seconds
    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")  # Format as MM:SS
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()


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

# Adding timing text (initially set to 25:00)
timer_text = canvas.create_text(100, 130, text="25:00", font=(FONT_NAME, 35, "bold"))

# Layout
canvas.grid(column=1, row=1)  # Use grid instead of pack

# Creating Timer label
timer_label = tkinter.Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# creating start button
start_button = tkinter.Button(text="Start", highlightbackground=YELLOW, highlightthickness=0, bg=YELLOW,
                              command=start_timer)
start_button.grid(column=0, row=3)

# creating a Restart button
restart_btn = tkinter.Button(text="Restart", highlightbackground=YELLOW, highlightthickness=0, bg=YELLOW)
restart_btn.grid(column=3, row=3)

# creating a check mark label
check_label = tkinter.Label(text="✓", fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=4)

# Keep the window open
window.mainloop()
