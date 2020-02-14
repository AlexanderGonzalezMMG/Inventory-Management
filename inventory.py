# !/usr/local/bin/env python3.8
import tkinter as tk
from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilenames
from tkinter import ttk
import numpy as np
from pathlib import Path
import pandas as pd
import os
import sys
import csv
# TODO: Add options to remove products, move category, add products, and etc.
# TODO: Create app window manager (main class).
# TODO: Document every function
# TODO: export into exe for mac/windows

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

initDir = "~/Desktop/Git/inventory-scripts/data"
files = [('CSV Files', '*.csv'), ('Excel Files',
                                  '*.xlsx'), ('Text Files', '*.txt')]



class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Malone Inventory Management")
        self.geometry("500x500")

        self.menubar = tk.Menu(self, bg="lightgrey", fg="white")
        self.file_menu = tk.Menu(self.menubar, tearoff=0, bg="lightgrey", fg="white")
        
        self.file_menu.add_command(label="Open", command=self.file_open, accelerator="Ctrl+O")
        self.file_menu.add_command(label="Save", command=self.file_open, accelerator="Ctrl+S")

        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.config(menu=self.menubar)
        
        
    def file_open(self, event=None):
        file = askopenfilenames()
        
        while file and not file.endswith(".csv"):
            msg.showerror("Wrong File Type, please load an csv or xlsx file!")
            file = askopenfilenames()
        

def save():
    file_name = asksaveasfilename(filetypes=files, defaultextension=files)
    return file_name

def remove_inventory(df, dfr):
    for row in df.itertuples():
        for remove_value in dfr.sku:
            if(row.sku == remove_value):
                df = df.drop([row.Index])
    file_name = save()
    df.to_csv(file_name, index=False)

def change_to_clearance(df,dfc):
    for row in df.itertuples():
        for sku in dfc.sku:
            if(row.sku == sku):
                if row.categories != 'Default Category/Clearance,Landmark Categories/Clearance':
                    df.loc['categories'] = 'Default Category/Clearance,Landmark Categories/Clearance'
                else:
                    print("Category: [{}] ".format(row.categories))
                    
    return df


if __name__ == "__main__":
    app = App()
    app.mainloop()


# root.inv_filepath = askopenfilenames(
#     initialdir=initDir, title="choose your inventory file", filetypes=files)
# inv_filepath = ''.join(root.inv_filepath)
# root.withdraw()

# df_inv = pd.read_csv(inv_filepath, engine="python", sep=',', quotechar='"', error_bad_lines=False)

# root.rem_filepath = askopenfilenames(
#     initialdir=initDir, title="choose your product removal file")
# rem_filepath = ''.join(root.rem_filepath)
# root.withdraw()

# # df_remove = pd.read_excel(rem_filepath, sheetName=None)
# # remove_inventory(df_inv, df_remove)


# # TODO: Turn this into a function that will be called by a button to open Clearance CSV file.
# df_change = pd.ExcelFile(rem_filepath)

# for name in df_change.sheet_names:
#     df = df_change.parse(name)
#     if name == 'REMOVED':
#         print('Done!\n')
#         break
#     elif df.empty == True:
#         print('Processing: [{}] ...'.format(name), 'Empty!')
#     else:
#         print('Processing: [{}] ...'.format(name))
#         df_inv = change_to_clearance(df_inv, df)

