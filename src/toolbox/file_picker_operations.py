import tkinter as tk
from tkinter import filedialog

DESTINATION = "fieldworks_files"


# Open system file explorer and return path of selected file
def file_picker():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    root.wm_attributes("-topmost", 1)
    return filedialog.askopenfilename()  # Open the file dialog


def select_file(title, file_types):
    return filedialog.askopenfilename(
        title=title, filetypes=file_types, defaultextension=".flextext"
    )


def save_file(title):
    return filedialog.asksaveasfilename(title=title, initialdir=DESTINATION)
