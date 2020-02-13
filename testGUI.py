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
# !/usr/local/bin/env python3.8

# TODO: Add options to remove products, move category, add products, and etc.
# TODO: Create app window manager (main class), export into exe for mac/windows.
# TODO: Start github and readme for project. Document every function


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def clean_inv(self):
        root.inv_filepath = askopenfilenames(
        initialdir=initDir, title="choose your inventory file")
        inv_filepath = ''.join(root.inv_filepath)
        root.withdraw()

    def change_cat(self):
        print("Changing Category")

    def add_products(self):
        print("Adding Products to Inv")

    def remove_inventory(df, dfr):
        for row in df.itertuples():
            for remove_value in dfr.sku:
                if(row.sku == remove_value):
                    df = df.drop([row.Index])
        file_name = asksaveasfilename(filetypes=files, defaultextension=files)
        df.to_csv(file_name, index=False)

    def create_widgets(self):
        self.clean_inv = tk.Button(self)
        self.clean_inv["text"] = "Clean Inventory"
        self.clean_inv["command"] = self.clean_inv
        self.clean_inv.pack(side="top")

        self.change_cat = tk.Button(self)
        self.change_cat["text"] = "Change Category"
        self.change_cat["command"] = self.change_cat
        self.change_cat.pack(side="top")

        self.add_products = tk.Button(self)
        self.add_products["text"] = "Change Category"
        self.add_products["command"] = self.add_products
        self.add_products.pack(side="top")

        self.quit = tk.Button(self, text="Cancel", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")


root = tk.Tk()
app = Application(master=root)
app.master.title("Inventory System")
app.master.geometry("300x300")
app.mainloop()
initDir = "/Users/alexgonzalez/Desktop/Git/"
files = [('CSV Files', '*.csv'), ('Text Document', '*.txt')]


"""
save is a function that is used to grab the filepath from the user in order to save
the modified data frames to csv
"""


"""
remove_inventory is a function that iterates over an inventory csv file, if a SKU # is in
the Remove xlsx file, the function will remove the row correspoding to the SKU #.
:param df: Inventory CSV file (Dataframe)
:param dfr: Products to be removed xlsx file (Dataframe)
"""


# TODO: clean this portion, add to main app class.




root.rem_filepath = askopenfilenames(
    initialdir=initDir, title="choose your product removal file")
rem_filepath = ''.join(root.rem_filepath)
root.withdraw()

print(inv_filepath, rem_filepath)

df_inventory = pd.read_csv(
    inv_filepath, engine="python", sep=',', quotechar='"', error_bad_lines=False)
df_remove = pd.read_excel(rem_filepath, sheetName=None)

remove_inventory(df_inventory, df_remove)
