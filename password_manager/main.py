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

# Create a Website name Entry
website_name = tkinter.Entry()
# Create Email/Username Entry
email_username = tkinter.Entry()
# Create a password Entry
password_entry = tkinter.Entry()
# create Generate Password Button
password_btn = tkinter.Button()
# Create Add Button
add_btn = tkinter.Button()



# keep the window in a loop
window.mainloop()
