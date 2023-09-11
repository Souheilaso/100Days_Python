import tkinter


def save_print():
    name = entry.get()
    print(name)


window = tkinter.Tk()
window.title("First GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)


my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()
my_label.grid(column=0, row=0)

greet = tkinter.Label(text="Python Rocks", fg="red")
# greet.pack()
greet.grid(column=2, row=0)

# buttons
button = tkinter.Button(text="Save", height=3, width=20, foreground="red", command=save_print)
button.grid(column=1, row=1)
# button.pack()

# Entry
entry = tkinter.Entry()
# entry.pack()
entry.grid(column=3, row=2)


window.mainloop()
