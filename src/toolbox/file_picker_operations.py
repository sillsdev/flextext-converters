import tkinter as tk
from tkinter import filedialog


# Open system file explorer and return path of selected file
def file_picker():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    return filedialog.askopenfilename()  # Open the file dialog
