from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilenames
from tkinter import ttk
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

root = Tk()
initDir = "/Users/alexgonzalez/Desktop/"
files = [('CSV Files', '*.csv'), ('Text Document', '*.txt')]


"""
save is a function that is used to grab the filepath from the user in order to save
the modified data frames to csv
"""


def save():
    file_name = asksaveasfilename(filetypes=files, defaultextension=files)
    return file_name


"""
remove_inventory is a function that iterates over an inventory csv file, if a SKU # is in 
the Remove xlsx file, the function will remove the row correspoding to the SKU #. 
:param df: Inventory CSV file (Dataframe)
:param dfr: Products to be removed xlsx file (Dataframe)
"""


def remove_inventory(df, dfr):
    for row in df.itertuples():
        for remove_value in dfr.sku:
            if(row.sku == remove_value):
                df = df.drop([row.Index])
    file_name = save()
    df.to_csv(file_name, index=False)


# TODO: clean this portion, add to main app class.
# ! Code Reads in Inventory CSV.
root.inv_filepath = askopenfilenames(
    initialdir=initDir, title="choose your inventory file")
inv_filepath = ''.join(root.inv_filepath)
root.withdraw()

df_inventory = pd.read_csv(inv_filepath, engine="python", sep=',', quotechar='"', error_bad_lines=False)




# root.rem_filepath = askopenfilenames(
#     initialdir=initDir, title="choose your product removal file")
# rem_filepath = ''.join(root.rem_filepath)
# root.withdraw()

# print(inv_filepath, rem_filepath)


# df_remove = pd.read_excel(rem_filepath, sheetName=None)

# remove_inventory(df_inventory, df_remove)
