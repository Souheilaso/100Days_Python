import tkinter
# ----------------------- PASSWORD GENERATOR ---------------------- #


# ----------------------- SAVE PASSWORD ---------------------- #
def save_details():
    website = website_name.get()
    password = password_entry.get()
    email = email_username.get()
# ----------------------- UI SETUP ---------------------- #


# create a window
window = tkinter.Tk()

# Window title
window.title("Password Manager")
window.config(padx=50, pady=50)

# creating a canvas
canvas = tkinter.Canvas(width=200, height=200)

# Finding the image
image = tkinter.PhotoImage(file="logo.png")

# creating the image location in the canvas
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Create Website Label
web_label = tkinter.Label(text="Website:")
web_label.grid(column=0, row=1)
# Create a Website name Entry
website_name = tkinter.Entry(width=35)
website_name.grid(column=1, row=1, columnspan=2)
# This will start a cursor and focus on the entry
website_name.focus()


# Create Email/username Label
email_user_label = tkinter.Label(text="Email/Username:")
email_user_label.grid(column=0, row=2)
# Create Email/Username Entry
email_username = tkinter.Entry(width=35)
email_username.grid(column=1, row=2, columnspan=2)
email_username.insert(0, "@gmail.com")

# Add a Password Label
password_label = tkinter.Label(text="Password:")
password_label.grid(column=0, row=3)
# Create a password Entry
password_entry = tkinter.Entry(width=18)
password_entry.grid(column=1, row=3, columnspan=1)


# create Generate Password Button
password_btn = tkinter.Button(text="Generate Password")
password_btn.grid(column=2, row=3)
# Create Add Button
add_btn = tkinter.Button(text="Add", width=36)
add_btn.grid(column=1, row=4, columnspan=2)


# keep the window in a loop
window.mainloop()
