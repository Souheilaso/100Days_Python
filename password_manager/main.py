import tkinter
# ----------------------- PASSWORD GENERATOR ---------------------- #


# ----------------------- SAVE PASSWORD ---------------------- #


# ----------------------- UI SETUP ---------------------- #


# create a window
window = tkinter.Tk()

# Window title
window.title("Password Manager")
window.config(padx=200, pady=200)

# creating a canvas
canvas = tkinter.Canvas(width=200, height=224)

# Finding the image
image = tkinter.PhotoImage(file="logo.png")

# creating the image location in the canvas
canvas.create_image(100, 112, image=image)




# keep the window in a loop
window.mainloop()
