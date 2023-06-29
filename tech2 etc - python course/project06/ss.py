import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()
canvas=tk.Canvas(root, width=300, height=300,)
canvas.pack()

def ss():
    screenshot=pyautogui.screenshot()
    saving=asksaveasfilename()
    screenshot.save(saving+"_screenshot.png")

button=tk.Button(text="click here to take a Screenshot", command=ss, font=10)
canvas.create_window(150,150,window=button)
tk.mainloop()