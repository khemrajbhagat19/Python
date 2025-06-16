import tkinter as tk

window=tk.Tk()
window.title("Listbox Example")
window.geometry('1260x1600')
listbox=tk.Listbox(window)
listbox.insert(1,"Option 1")
listbox.insert(2,"Option 2")
listbox.insert(3,"Option 3")
listbox.pack()
window.mainloop()