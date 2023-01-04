import tkinter as tk
from tkinter import filedialog
from math import fabs
import os
import pandas as pd
import pathlib
from xlsxwriter.utility import xl_rowcol_to_cell
from gfs_report import CreateExcelReport
from gfs_main import GetFileSizes

# Create a GUI window using Tkinter
window = tk.Tk()

# Set the window size and position
window.geometry("900x500+200+200")

window.title("Giant File Safari")

# Set the background color of the GUI window
window.configure(bg="#E6E6E6")

# Text explanation of what the program does and what each input field means
tk.Label(window, text="Welcome to Giant File Safari!\n\nThis program lists the largest files in a folder and its subfolders.\n\nEnter the folder path, output folder, minimum file size, and the number of top results to be shown.\n\nHappy Hunting!",
         font=("Verdana", 12), bg="#E6E6E6", fg="black", padx=10, pady=10).grid(row=0, column=0, columnspan=3)

tk.Label(window, text="", bg="#E6E6E6", padx=10,
         pady=10).grid(row=1, column=0, columnspan=3)

# Create input fields for the path, output, minimum size, and top values
tk.Label(window, text="Path - the location of the folder to be analysed:",
         font=("Verdana", 11), bg="#E6E6E6", fg="black").grid(row=2, column=0)
path = tk.StringVar()
e1 = tk.Entry(window, textvariable=path, font=("Verdana", 11), bg="white")
e1.grid(row=2, column=1, padx=10, pady=10)

tk.Label(window, text="Output folder - the location of the final report:",
         font=("Verdana", 11), bg="#E6E6E6", fg="black").grid(row=3, column=0)
output = tk.StringVar()
e2 = tk.Entry(window, textvariable=output, font=("Verdana", 11), bg="white")
e2.grid(row=3, column=1, padx=10, pady=10)

tk.Label(window, text="Minimum size of file (GB):", font=(
    "Verdana", 11), bg="#E6E6E6", fg="black").grid(row=4, column=0)
minsize = tk.DoubleVar()
minsize.set(0.1)  # Set the initial value of minsize to 100MB
e3 = tk.Entry(window, textvariable=minsize, font=("Verdana", 11), bg="white")
e3.grid(row=4, column=1, padx=10, pady=10)

tk.Label(window, text="Top - largest files to list in the report:",
         font=("Verdana", 11), bg="#E6E6E6", fg="black").grid(row=5, column=0)
top = tk.IntVar()
top.set(100)  # Set the initial value of top to 100 entries
e4 = tk.Entry(window, textvariable=top, font=("Verdana", 11), bg="white")
e4.grid(row=5, column=1, padx=10, pady=10)

# Create browse buttons for the path and output fields
def browse_button_path():
    # Allow the user to select a directory and store it in the path variable
    filename = filedialog.askdirectory()
    path.set(filename)

def browse_button_output():
    # Allow the user to select a directory and store it in the output variable
    filename = filedialog.askdirectory()
    output.set(filename)

b1 = tk.Button(
    window,
    text="Browse",
    font=("Verdana", 10, "bold"),
    command=browse_button_path,
    bg="dark grey",
    fg="black",
    padx=10,
    pady=3,
)
b1.grid(row=2, column=2)

b2 = tk.Button(
    window,
    text="Browse",
    font=("Verdana", 10, "bold"),
    command=browse_button_output,
    bg="dark grey",
    fg="black",
    padx=10,
    pady=3,

)
b2.grid(row=3, column=2)

# Create a submit button that calls the GetFileSizes function

def submit():
    # Get the values entered by the user
    path_value = path.get()
    output_value = output.get()
    minsize_value = minsize.get()
    top_value = top.get()
    # Close the window
    window.destroy()

    # Call the GetFileSizes function
    GetFileSizes(path=path_value, output=output_value,
                 minsize=minsize_value, top=top_value)

b2 = tk.Button(
    window,
    text="Submit",
    font=("Verdana", 12, "bold"),
    bg="dark grey",
    fg="black",
    command=submit,
    padx=70,
    pady=20,
)

b2.grid(row=6, column=1, padx=10, pady=10)

# Start the GUI event
window.mainloop()
