from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilenames
from tkinter import ttk
import tkinter as tk
from tkinter import *
import numpy as np
from pathlib import Path
import pandas as pd
import os
import sys
import csv
# !/usr/local/bin/env python3.8

initDir = "/Users/alexgonzalez/Desktop/Git/inventory-scripts/data"
files = [('CSV Files', '*.csv'), ('Text Document', '*.txt')]


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Open CSV File"
        self.hi_there["command"] = self.open_csv
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def open_csv(self):
        self.filepath = askopenfilenames(
            initialdir=initDir, title="choose your inventory file")
        self.filepath=''.join(self.filepath)
        fp = open(self.filepath)
        read = csv.reader(fp,delimiter = ",")
        columns = next(read)
        print
        for name in columns:
            new_label = tk.Label(self, text=name)
            new_label.pack()

root = tk.Tk()
app = Application(master=root)
app.mainloop()
