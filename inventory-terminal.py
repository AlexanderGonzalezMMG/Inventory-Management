# !/usr/local/bin/env python3.8
from tkinter import *
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as msg
from tkinter import ttk
import tkinter as tk
import numpy as np
from pathlib import Path
import pandas as pd
import os
import sys
import csv
import logging
from datetime import datetime


def save():
    file_name = asksaveasfilename(filetypes=files, defaultextension=files)
    return file_name


def remove_inventory(df, dfr):
    for row in df.itertuples():
        for remove_value in dfr.sku:
            if(row.sku == remove_value):
                print(row)
                df = df.drop([row.Index])

    # file_name = save()
    return df


def change_to_clearance(df, dfc):
    for row in df.itertuples():
        for sku in dfc.sku:
            if(row.sku == sku):
                if row.categories != 'Default Category/Clearance,Landmark Categories/Clearance':
                    df.loc['categories'] = 'Default Category/Clearance,Landmark Categories/Clearance'
                else:
                    print("Category: [{}] ".format(row.categories))

    return df



initDir = "~/Desktop/Git/inventory-scripts/data"
files = [('CSV Files', '*.csv'), ('Excel Files',
                                  '*.xlsx'), ('Text Files', '*.txt')]


root = tk.Tk()
print("Please import your inventory csv file.")
root.withdraw()

root.inv_filepath = askopenfilename(
    initialdir=initDir, title="choose your inventory file", filetypes=files)
inv_filepath = ''.join(root.inv_filepath)
root.withdraw()

df_inv = pd.read_csv(inv_filepath, engine="python", sep=',',
                     quotechar='"', error_bad_lines=False)


print("Please import your csv file containing sku's to be removed.")
root.rem_filepath = askopenfilename(
    initialdir=initDir, title="choose your product removal file")
rem_filepath = ''.join(root.rem_filepath)
root.withdraw()

df_remove = pd.read_excel(rem_filepath, sheetName=None)
df_inv = remove_inventory(df_inv, df_remove)


# TODO: Turn this into a function that will be called by a button to open Clearance CSV file.
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


print("Done exporting inventory file... " +
      str(datetime.now().strftime("%Y%m%d-%H%M%S_"))+"cleaned_inv.csv")
df_inv.to_csv("./export/"+str(datetime.now().strftime("%Y%m%d-%H%M%S_")) +
              "cleaned_inv.csv", index=False)
