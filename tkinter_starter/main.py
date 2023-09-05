import tkinter
window = tkinter.Tk()
window.title("First GUI")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

greet = tkinter.Label(text="Python Rocks", fg="red")
greet.pack()

# buttons
button = tkinter.Button(text="click me", height=3, width=20, foreground="red")
button.pack()





window.mainloop()