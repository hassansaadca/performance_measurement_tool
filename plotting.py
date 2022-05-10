import tkinter as tk
import os
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


os.system('clear')

root = tk.Tk()
root.title("Test Program")
root.geometry('400x600')


myLabel = tk.Label(root, text = 'Enter your first name:')
myLabel.pack()

def greet():
    hello_label = tk.Label(root, text= f'Hello {myTextBox.get()}! Welcome to the shitshow!')
    hello_label.pack()

def plot_file():
    string1 = 'text-D3A4E18FD759-1.txt'
    fig, ax  = plt.subplots(2,1, figsize = (5, 5), dpi = 100, sharex = True)
    data = pd.read_csv(string1, sep = ';', index_col = 0)

    ax[0].plot(data.index ,data.x, color = 'red')
    ax[1].plot(data.index, data.y, color = 'blue')

    # plotting the graph
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master = root)
    canvas.draw()
    # placing the canvas on the Tkinter root
    canvas.get_tk_widget().pack()
    # creating the Matplotlib toolbar
    # toolbar = NavigationToolbar2Tk(canvas, root)
    # toolbar.update()
    # placing the toolbar on the Tkinter root
    # canvas.get_tk_widget().pack()


myTextBox = tk.Entry(root, width = 30)
myTextBox.pack()

myButton = tk.Button(root, text = 'Submit', command = greet)
myButton.pack()

plotButton= tk.Button(root, text = 'plot', command = plot_file)
plotButton.pack()


root.mainloop()
