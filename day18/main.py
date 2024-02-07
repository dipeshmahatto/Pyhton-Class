import tkinter as tk
from tkinter import ttk
window = tk.Tk()
# window.geometry("500*300")
window.minsize(width=500,height=400)

# Textfield
my_textfield = ttk.Entry(master=window)
my_textfield.place(x=100,y=100)

# Button
def my_button_handler():
    text_field_value = my_textfield.get()
    print(text_field_value)


my_button = ttk.Button(master= window, text = "Click Me",command=my_button_handler)
my_button.place(x= 100,y=150)

window.mainloop()