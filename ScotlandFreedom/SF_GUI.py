import tkinter as tk
from tkinter import filedialog
from math import fabs
import os
import pandas as pd
import pathlib
from xlsxwriter.utility import xl_rowcol_to_cell
from SF_Write_Report import CreateExcelReport
from SF_Main import GetFileSizes

# Create a GUI window using Tkinter
window = tk.Tk()
window.title("Scotland Freedom")

# Create a text explanation of what the program does and what each input field means
tk.Label(window, text="This program lists the largest files in a folder and its subfolders. Enter the folder path, output folder, minimum file size, and the number of top results to be shown.").grid(row=0, column=0, columnspan=3)

# Create input fields for the path, output, minimum size, and top values
tk.Label(window, text="Path:").grid(row=1, column=0)
path = tk.StringVar()
e1 = tk.Entry(window, textvariable=path)
e1.grid(row=1, column=1, padx=10, pady=10)

tk.Label(window, text="Output:").grid(row=2, column=0)
output = tk.StringVar()
e2 = tk.Entry(window, textvariable=output)
e2.grid(row=2, column=1, padx=10, pady=10)

tk.Label(window, text="Minimum size (GB):").grid(row=3, column=0)
minsize = tk.DoubleVar()
e3 = tk.Entry(window, textvariable=minsize)
e3.grid(row=3, column=1, padx=10, pady=10)

tk.Label(window, text="Top:").grid(row=4, column=0)
top = tk.IntVar()
e4 = tk.Entry(window, textvariable=top)
e4.grid(row=4, column=1, padx=10, pady=10)

# Create a browse button for the path input field
def browse_button():
    # Allow the user to select a directory and store it in the path variable
    filename = filedialog.askdirectory()
    path.set(filename)
    
b1 = tk.Button(window, text="Browse", command=browse_button)
b1.grid(row=1, column=2, padx=10, pady=10)

# Create a submit button that calls the GetFileSizes function
def submit():
    # Get the values entered by the user
    path_value = path.get()
    output_value = output.get()
    minsize_value = minsize.get()
    top_value = top.get()
    
    # Call the GetFileSizes function
    GetFileSizes(path=path_value, output=output_value, minsize=minsize_value, top=top_value)
    
b2 = tk.Button(window, text="Submit", command=submit)
b2.grid(row=5, column=1, padx=10, pady=10)

# Start the GUI event
window.mainloop()