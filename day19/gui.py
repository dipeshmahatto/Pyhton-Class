import tkinter as tk 
from tkinter import ttk , font

window = tk.Tk()
window.title("This is the first GUI Program in python")
window.minsize(width=500,height=400)

my_textfield_first = ttk.Entry(master=window)
my_textfield_first.place(x=100,y=100)

my_textfield_second = ttk.Entry(master=window)
my_textfield_second.place(x=100,y=150)

def my_button_handler():
    num_1 = my_textfield_first.get()
    num_2 = my_textfield_second.get()
    sum = int(num_1)+int(num_2)
    print("The sum is :",sum)
    
    result_label.configure(text = "Result ="+str(sum))

my_button = ttk.Button(master= window, text = "Add",command=my_button_handler)
my_button.place(x= 100,y=200)

result_label = ttk.Label(master=window,text="Result=",font = font.Font(size=25))

result_label.place(x=100,y=250)

window.mainloop()