import os
import tkinter as tk
from tkinter import filedialog


# Open system file explorer and return path of selected file
def file_picker():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    root.wm_attributes("-topmost", 1)
    return filedialog.askopenfilename()  # Open the file dialog


def select_file(title, file_types):
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    return filedialog.askopenfilename(
        title=title,
        filetypes=file_types,
        initialdir=downloads_folder,
        defaultextension=".flextext",
    )


def save_file(title, initialdir):
    return filedialog.asksaveasfilename(title=title, initialdir=initialdir)
