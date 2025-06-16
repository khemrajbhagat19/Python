import tkinter as tk

window=tk.Tk()
window.title("Radiobutton Example")
window.geometry('800x200')
radio_var=tk.StringVar()
radiobutton1=tk.Radiobutton(window,text="Male",variable=radio_var,value="male")
radiobutton2=tk.Radiobutton(window,text="Female",variable=radio_var,value="female")
radiobutton1.pack()
radiobutton2.pack()
window.mainloop()