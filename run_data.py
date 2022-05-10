import tkinter as tk
import os
from tkinter import filedialog
import pandas as pd
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
from time import sleep
import numpy as np


class File():

    def __init__(self, root):
        self.base = root
        self.filepath = ''
        self.data = pd.DataFrame()
        self.max_g = 0.011
        self.baseline_x = 0
        self.baseline_y = 0
        self.baseline_z = 0
        pass

    def assign(self):
        self.filepath = tk.filedialog.askopenfilename() #Why do i have to include tk. in this. I already imported filedialog up top
        print('CURRENT FILEPATH: ' , self.filepath)


    def create_data(self):
        self.data = pd.read_csv(self.filepath, sep = ';', index_col = 0)
        self.data['seconds'] = self.data.index/30
        self.data = self.data[['seconds','x','y','z']]
        self.data.x = self.data.x - self.baseline_x
        self.data.y = self.data.y - self.baseline_y
        self.data.z = self.data.z - self.baseline_z
        self.plot_intervals = np.arange(0, int(self.data.seconds.max())+2, 1)


    def plot_data(self):
        try:
            self.canvas.get_tk_widget().pack_forget()
        except:
            pass

        try:
            self.no_figure_warning.destroy()
        except:
            pass

        self.fig, self.ax  = plt.subplots(3,1, figsize = (20, 20), dpi = 100, sharex = True)
        plt.xticks(self.plot_intervals)

        #plot x data
        self.ax[0].plot(self.data.seconds ,self.data.x, color = 'green', linewidth = .7)
        self.ax[0].set_title('X (Rail to Rail)', size = 10)
        self.ax[0].grid(axis = 'x', which = 'both')
        self.ax[0].set_ylabel('Acceleration (G)', size = 8)


        #plot y data
        self.ax[1].plot(self.data.seconds, self.data.y, color = 'red', linewidth = .7)
        self.ax[1].set_title('Y (Front to Back)', size = 10)
        self.ax[1].grid(axis = 'x', which = 'both')
        self.ax[1].set_ylabel('Acceleration (G)', size = 8)

        #plot z data
        self.ax[2].plot(self.data.seconds, self.data.z, color = None, linewidth = .7)
        self.ax[2].set_title('Z', size = 10)
        self.ax[2].grid(axis = 'x', which = 'both')
        self.ax[2].set_ylabel('Acceleration (G)', size = 8)


        self.data['xmin'] = self.data.seconds[(self.data.x.shift(1) > self.data.x) & (self.data.x.shift(-1) > self.data.x) & (self.data.x < -1* self.max_g)]
        self.data['xmax'] = self.data.seconds[(self.data.x.shift(1) < self.data.x) & (self.data.x.shift(-1) < self.data.x) & (self.data.x > self.max_g)]
        self.data['ymin'] = self.data.seconds[(self.data.y.shift(1) > self.data.y) & (self.data.y.shift(-1) > self.data.y) & (self.data.y < -1* self.max_g)]
        self.data['ymax'] = self.data.seconds[(self.data.y.shift(1) < self.data.y) & (self.data.y.shift(-1) < self.data.y) & (self.data.y > self.max_g)]

        self.ax[0].scatter(self.data.xmin ,self.data.x, color = 'green', marker = 'o', s = 5)
        self.ax[0].scatter(self.data.xmax ,self.data.x, color = 'green', marker = 'o', s = 5)
        self.ax[1].scatter(self.data.ymin ,self.data.y, color = 'red', marker = 'o', s = 5)
        self.ax[1].scatter(self.data.ymax ,self.data.y, color = 'red', marker = 'o', s = 5)


        #set shared x label
        self.ax[2].set_xlabel('Elapsed Time (Seconds)', size = 10)

        self.canvas = FigureCanvasTkAgg(self.fig, master = self.base)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    def clear_screen(self):
        try:
            self.canvas.get_tk_widget().pack_forget()
        except:
            pass

        try:
            self.no_figure_warning.destroy()
        except:
            pass



    def save_plots(self):
        try:
            self.fig.savefig('chart1.png', dpi = 800)
        except:
            self.no_figure_warning = tk.Label(self.base, text = 'You have not yet created a figure!')
            self.no_figure_warning.pack()



    def plot_lines(self): #####
        #plot x horizontal lines to x chart
        self.ax[0].axhline(y = self.max_g, linestyle = ':', linewidth = 0.5, color = 'grey')
        self.ax[0].axhline(y = -1* self.max_g, linestyle = ':', linewidth = 0.5, color = 'grey')
        self.ax[0].axhline(y = 0, linestyle = '-', linewidth = .5, color = 'black')

        #add horizontal lines to y chart
        self.ax[1].axhline(y = self.max_g, linestyle = ':', linewidth = 0.5, color = 'grey')
        self.ax[1].axhline(y = -1* self.max_g, linestyle = ':', linewidth = 0.5, color = 'grey')
        self.ax[1].axhline(y = 0, linestyle = '-', linewidth = .5, color = 'black')

        #add horizontal lines to y chart
        self.ax[2].axhline(y = 0, linestyle = '-', linewidth = .5, color = 'black')


    def create_and_plot(self):
        self.create_data()
        self.plot_data()
        self.plot_lines()
