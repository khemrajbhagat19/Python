import tkinter as tk
from tkinter import colorchooser

def choose_colour():
    color_code=colorchooser.askcolor(title="Choose a colour")
    print(color_code)

root=tk.Tk()
root.title("Colour Picker Example")
root.geometry("800x200")

button=tk.Button(root,text="Choose colour",command=choose_colour)
button.pack()

root.mainloop()