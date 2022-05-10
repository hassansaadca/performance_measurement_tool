import tkinter as tk
from tkinter import filedialog
import pandas as pd

base = tk.Tk()
# Create a canvas
base.geometry('400x400')
# Function for opening the file

b1 = tk.Button(base, text = 'Button 1')
b1.grid(row = 1, column = 1)

b2 = tk.Button(base, text = 'Button 2')
b2.grid(row = 2, column = 1)

b3 = tk.Button(base, text = 'Button 3')
b3.grid(row = 1, column = 2)

b4 = tk.Button(base, text = 'Button 4')
b4.grid(row = 2, column = 5)

b5= tk.Button(base, text = 'Button 5')
b5.pack()

base.mainloop()
