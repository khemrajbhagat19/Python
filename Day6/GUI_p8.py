import tkinter as tk

window=tk.Tk()
window.title("Spinbox Example")
window.geometry('800x200')
scale=tk.Spinbox(window,from_=0,to=10)
scale.pack()
window.mainloop()