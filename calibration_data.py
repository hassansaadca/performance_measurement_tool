import tkinter as tk
import os
from tkinter import filedialog
import pandas as pd
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt
from time import sleep
import numpy as np

class Calibrate():

    def __init__(self):
        self.filepath = ''
        self.data = pd.DataFrame()
        self.baseline_x = 0
        self.baseline_y = 0
        self.baseline_z = 0
        pass

    def set_baseline(self):
        self.filepath =  tk.filedialog.askopenfilename() #Why do i have to include tk. in this. I already imported filedialog up top
        self.data = pd.read_csv(self.filepath, sep = ';', index_col = 0)
        self.data['seconds'] = self.data.index/30
        self.data = self.data[['seconds','x','y','z']]
        self.baseline_x = self.data.x.mean()
        self.baseline_y = self.data.y.mean()
        self.baseline_z = self.data.z.mean()
        print('CURRENT FILEPATH: ' , self.filepath)
        print('X Baseline: ', self.baseline_x)
        print('Y Baseline: ', self.baseline_y)
        print('Z Baseline: ', self.baseline_z)
