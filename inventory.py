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
from datetime import datetime
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
#.
the Remove xlsx file, the function will remove the row correspoding to the SKU
:param df: Inventory CSV file (Dataframe)
:param dfr: Products to be removed xlsx file (Dataframe)
"""

initDir = "~/Desktop/Git/inventory-scripts/data"
files = [('CSV Files', '*.csv'), ('Excel Files',
                                  '*.xlsx'), ('Text Files', '*.txt')]

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.inv_file_name = None
        self.inv_df = None

        self.cleaner_file_name = None
        self.df_remove = None

        self.title("Malone Inventory Management")
        self.geometry("300x300")

        self.open_file_btn = ttk.Button(
            self, text='Import Inventory file', command=self.file_open)
        self.open_file_btn.pack()

        self.open_rem_file_btn = ttk.Button(
            self, text='Import Skus to be removed file', command=self.file_open)
        self.open_rem_file_btn.pack()

        self.save_btn = ttk.Button(
            self, text='Export clean Inventory file', command=self.save)
        self.save_btn.pack()

        self.menubar = tk.Menu(self, bg="lightgrey", fg="black")
        self.file_menu = tk.Menu(
            self.menubar, tearoff=0, bg="lightgrey", fg="black")

        self.file_menu.add_command(
            label="Open", command=self.file_open, accelerator="Ctrl+O")
        self.file_menu.add_command(
            label="Save", command=self.file_open, accelerator="Ctrl+S")

        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.config(menu=self.menubar)

        self.bind("<Control-o>", self.file_open)
        self.bind("<Control-s>", self.save)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def file_open(self, event=None):
        file = askopenfilename()

        if not self.inv_file_name:
            if file.endswith(".csv"):
                self.inv_df = pd.read_csv(file, engine="python",
                                          sep=',', quotechar='"', error_bad_lines=False)
            elif file.endswith(".xlsx"):
                self.df_remove = pd.read_excel(file, sheetName=None)
            self.inv_file_name = file
        else:
            if file.endswith(".csv"):
                self.df_remove = pd.read_csv(file, engine="python",
                                             sep=',', quotechar='"', error_bad_lines=False)
            elif file.endswith(".xlsx"):
                self.df_remove = pd.read_excel(file, sheetName=None)
            self.cleaner_file_name = file

    def on_closing(self):
        if msg.askokcancel("quit", "Do you want to quit?"):
            self.destroy()

    def save(self):
        self.remove_inventory(self.inv_df, self.df_remove)

    def remove_inventory(self,df, dfr):
        for row in df.itertuples():
            for remove_value in dfr.sku:
                if(row.sku == remove_value):
                    df = df.drop([row.Index])

        df_inv.to_csv(str(datetime.now().strftime(
            "%Y%m%d-%H%M%S_"))+"cleaned_inv.csv", index=False)

    def change_to_clearance(df, dfc):
        for row in df.itertuples():
            for sku in dfc.sku:
                if(row.sku == sku):
                    if row.categories != 'Default Category/Clearance,Landmark Categories/Clearance':
                        df.loc['categories'] = 'Default Category/Clearance,Landmark Categories/Clearance'
                    else:
                        print("Category: [{}] ".format(row.categories))

        return df


if __name__ == "__main__":
    filenames = []
    app = App()
    app.mainloop()


# root.inv_filepath = askopenfilename(
#     initialdir=initDir, title="choose your inventory file", filetypes=files)
# inv_filepath = ''.join(root.inv_filepath)
# root.withdraw()

# df_inv = pd.read_csv(inv_filepath, engine="python", sep=',', quotechar='"', error_bad_lines=False)

# root.rem_filepath = askopenfilename(
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
