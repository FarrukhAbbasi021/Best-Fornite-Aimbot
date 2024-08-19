import tkinter as tk
from tkinter import *
import os

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

os.system("title SQUARE - SMALL")
print("Close This Window To Close FOV Square")

def create():
    r = tk.Tk()
    r.wm_attributes("-topmost", True)
    r.wm_attributes("-disabled", True)
    r.wm_attributes("-transparentcolor", "white")
    r.overrideredirect(True)
    r.lift()
    width = 250
    height = 250
    w = Canvas(r, width=width, height=height)
    w.create_rectangle(0, 0, width, height, fill="white", outline = 'white')
    w.pack()
    center(r)
    r.mainloop()

create()