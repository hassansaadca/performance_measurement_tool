import tkinter as tk
import os
from tkinter import filedialog
import pandas as pd
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
from time import sleep
import numpy as np

import run_data
import calibration_data

os.system('clear')


base = tk.Tk()
base.geometry('1200x800')
base.title('G Force Plotting')

#--------------------------------------------------------------------------------------------------------------

file1 = run_data.File(base)

#import file
b1 = tk.Button(base,text="Upload File",font=40, command= file1.assign)
b1.place(x = 10, y = 10)


#plot data
b2 = tk.Button(base,text="Display Data",font=40,command= file1.create_and_plot)
b2.place(x = 10, y = 40)


#clear screen
b3 = tk.Button(base,text="Clear Screen",font=40,command= file1.clear_screen)
b3.place(x = 200, y = 10)

#save figure
b4 = tk.Button(base,text="Save Figure",font=40,command= file1.save_plots)
b4.place(x = 200, y = 40)

# Calibrate the dataset-------------------------------

calibration_file = calibration_data.Calibrate()


def calibrate():
    calibration_file.set_baseline()
    file1.baseline_x = calibration_file.baseline_x
    file1.baseline_y = calibration_file.baseline_y
    file1.baseline_z = calibration_file.baseline_z
    file1.create_and_plot()


b0 = tk.Button(base, text = 'Calibrate', font = 40, command = calibrate)
b0.place(x = 800, y = 10)


# Set new max acceptable G force--------------------------------

lab1 = tk.Label(base, text = 'Max acceptable milli-G: ')
lab1.pack()

tb1 = tk.Entry(base, width = 20)
tb1.pack()

def assign_max_g(some_file):
    some_file.max_g = int(tb1.get())/1000
    some_file.create_and_plot()

b_tb1 = tk.Button(base, text = 'New Max G', font = 40, command = lambda: assign_max_g(file1))
b_tb1.pack()



###------------------------------------------------------------




base.mainloop()
