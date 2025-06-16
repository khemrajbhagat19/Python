import tkinter as tk

window=tk.Tk()
window.title("Checkbutton Example")
window.geometry('800x200')
check_var=tk.BooleanVar()
checkbutton=tk.Checkbutton(window,text="Check me",variable=check_var)
checkbutton.pack()
window.mainloop()