# This is a simple GUI program using tkinter

from tkinter import *

def button_clicked():
    print("Button clicked!")
    new_text = input_field.get()    # Get the entry text
    my_label.config(text=new_text)  # Update the label


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# Entry
input_field = Entry(width=10)
input_field.grid(column=3, row=2)

window.mainloop()