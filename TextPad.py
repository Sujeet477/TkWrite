# Import tkinter for creating GUI apps

import tkinter as tk
from tkinter import filedialog, messagebox

# Main window code
root = tk.TK()
root.title("Basic Text Editor")
root.geometry("800x600")

# Create text area
text = tk.Text(
    root,
    wrap = tk.WORD,
    font = ("Helvetica", 20)
)

text.pack(expand = True, fill = tk.BOTH)

# Main logic 

# Function 1-to create a new file
def new_file():
    text.delete(1.0, tk.END)

# Function -2 to open a new file
def open_file():
    # open file dialouge
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        # open selected file
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

# function 3 - save a file

def save_file():
    # open save file dialoge
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))

    messagebox.showinfo("Info", "File saved successfully")

