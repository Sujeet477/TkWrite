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