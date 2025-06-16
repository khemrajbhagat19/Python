import tkinter as tk
root=tk.Tk()
root.title("Frame Example")
root.geometry("800x200")

frame=tk.Frame(root,bg="yellow",width=200,height=100)
frame.pack()


root.mainloop()