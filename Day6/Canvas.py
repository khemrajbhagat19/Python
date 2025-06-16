import tkinter as tk
root=tk.Tk()
root.title("Canvas Example")

canvas=tk.Canvas(root,width=400,height=400)
canvas.pack()

canvas.create_line(100,100,200,100)
canvas.create_rectangle(50,50,150,150,fill="blue")
canvas.create_rectangle(100,100,300,300,fill="blue")

root.mainloop()