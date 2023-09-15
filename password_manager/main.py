import tkinter
# ----------------------- PASSWORD GENERATOR ---------------------- #


# ----------------------- SAVE PASSWORD ---------------------- #


# ----------------------- UI SETUP ---------------------- #


# create a window
window = tkinter.Tk()

# Window title
window.title("Password Manager")
window.config(padx=30, pady=30)

# creating a canvas
canvas = tkinter.Canvas(width=200, height=200)

# Finding the image
image = tkinter.PhotoImage(file="logo.png")

# creating the image location in the canvas
canvas.create_image(120, 100, image=image)
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

# Add a Password Label
password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)
# Create a password Entry
password_entry = tkinter.Entry()
password_entry.grid(column=1, row=3)


# create Generate Password Button
password_btn = tkinter.Button(text="Generate Password")
password_btn.grid(column=2, row=3)
# Create Add Button
add_btn = tkinter.Button(text="Add")
add_btn.grid(column=1, row=4)



# keep the window in a loop
window.mainloop()
