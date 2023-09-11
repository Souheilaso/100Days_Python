import tkinter

# setting up window
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)

# Creating an Entry
entry = tkinter.Entry()
entry.grid(column=1, row=0)

# Creating label 1
miles_label = tkinter.Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)