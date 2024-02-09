import tkinter as tk 
from tkinter import ttk , font

window = tk.Tk()
window.title("This is the first GUI Program in python")
window.minsize(width=500,height=400)

result_label1 = ttk.Label(master=window,text="First Number :",font = font.Font(size=15))
result_label1.grid(row=0,column=0,pady=10)

my_textfield_first = ttk.Entry(master=window,font = font.Font(size=15))
my_textfield_first.grid(row=0,column=1,pady=10)

result_label2 = ttk.Label(master=window,text="Second Number :",font = font.Font(size=15))
result_label2.grid(row=1,column=0,pady=10)

my_textfield_second = ttk.Entry(master=window,font = font.Font(size=15))
my_textfield_second.grid(row=1,column=1,pady=10)

def my_button_handler():
    num_1 = my_textfield_first.get()
    num_2 = my_textfield_second.get()
    sum = int(num_1)+int(num_2)
    # print("The sum is :",sum)
    
    result_label.configure(text = "Result ="+str(sum))

my_button = ttk.Button(master= window, text = "Add",command=my_button_handler)
my_button.grid(row=2,column=1,pady=10)

result_label = ttk.Label(master=window,text="Result=",font = font.Font(size=25))
result_label.grid(row=3,column=0,pady=10)

window.mainloop()