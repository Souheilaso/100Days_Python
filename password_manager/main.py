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

# Create Website Label
web_label = tkinter.Label(text="Website:")
web_label.grid(column=0, row=1)
# Create a Website name Entry
website_name = tkinter.Entry()
website_name.grid(column=1, row=1)


# Create Email/username Label
email_user_label = tkinter.Label(text="Email/Username:")
email_user_label.grid(column=0, row=2)
# Create Email/Username Entry
email_username = tkinter.Entry()
email_username.grid(column=1, row=2)

# Create a password Entry
password_entry = tkinter.Entry()


# create Generate Password Button
password_btn = tkinter.Button(text="Generate Password")
# Create Add Button
add_btn = tkinter.Button(text="Add")



# keep the window in a loop
window.mainloop()
