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

# creating second row label
equal_label = tkinter.Label(text="is equal to", font=("Arial", 24, "bold"))
equal_label.grid(column=0, row=1)

# creating column 1 label
number_label = tkinter.Label(text=0, font=("Arial", 24, "bold"))
number_label.grid(column=1, row=1)

# creating column 2, row 1 label
km_label = tkinter.Label(text="Km", font=("Arial", 24, "bold"))
km_label.grid(column=2, row=1)

window.mainloop()
