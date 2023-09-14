import tkinter
# ----------------------- PASSWORD GENERATOR ---------------------- #


# ----------------------- SAVE PASSWORD ---------------------- #


# ----------------------- UI SETUP ---------------------- #


# create a window
window = tkinter.Tk()

# Window title
window.title("Password Manager")
window.config(padx=100, pady=100)

# creating a canvas
canvas = tkinter.Canvas(width=500, height=500)

# Finding the image
image = tkinter.PhotoImage(file="logo.png")

# creating the image location in the canvas
canvas.create_image(250, 200, image=image)
canvas.grid(column=1, row=0)



# keep the window in a loop
window.mainloop()
