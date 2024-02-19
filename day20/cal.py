import tkinter as tk
from tkinter import ttk
from tkinter import font

window = tk.Tk()
window.minsize(width=500,height=400)
window.resizable(0,0);
window.title("Python Calculator!")

buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    '0', 'C', '.', '/',
    '='
];


window.rowconfigure((0, 1, 2, 3), weight = 1)
window.columnconfigure((0, 1, 2, 3), weight = 1)

input = ttk.Entry(master = window)
input.grid(row = 0, column = 0, columnspan = 4, sticky = "nsew")

row = 1
col = 0

for i in range(len(buttons)):
    button = ttk.Button(master = window, text = buttons[i])
    button.grid(row = row, column = col)
    col += 1
    if col == 4:
        row += 1
        col = 0



window.mainloop()