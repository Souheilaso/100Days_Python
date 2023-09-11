import tkinter


def save_print():
    name = entry.get()
    print(name)


window = tkinter.Tk()
window.title("First GUI")
window.minsize(width=500, height=300)


my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()
my_label.grid(column=0, row=0)

greet = tkinter.Label(text="Python Rocks", fg="red")
# greet.pack()

# buttons
button = tkinter.Button(text="Save", height=3, width=20, foreground="red", command=save_print)
# button.pack()

# Entry
entry = tkinter.Entry()
# entry.pack()


window.mainloop()
