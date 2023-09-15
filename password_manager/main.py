import tkinter
import tkinter.messagebox
import random


# ----------------------- PASSWORD GENERATOR ---------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)] + \
                    [random.choice(symbols) for _ in range(nr_symbols)] + \
                    [random.choice(numbers) for _ in range(nr_numbers)]  # Corrected this line

    random.shuffle(password_list)

    password = "".join(password_list)


# ----------------------- SAVE PASSWORD ---------------------- #
def save_details():
    website = website_name.get()
    password = password_entry.get()
    email = email_username.get()

    if website and password and email:
        with open("passwords.txt", "a") as file:
            data = f"{website} | {email} | {password}\n"
            file.write(data)

        website_name.delete(0, tkinter.END)
        password_entry.delete(0, tkinter.END)
        email_username.delete(0, tkinter.END)

    if len(website) == 0 or len(password) == 0:
        tkinter.messagebox.showerror("Error", "Please fill in all fields.")
    else:
        tkinter.messagebox.showinfo(website, "Password details saved successfully.")


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
password_btn = tkinter.Button(text="Generate Password", command=generate_password)
password_btn.grid(column=2, row=3)
# Create Add Button
add_btn = tkinter.Button(text="Add", width=36, command=save_details)
add_btn.grid(column=1, row=4, columnspan=2)

# keep the window in a loop
window.mainloop()
