'''from tkinter import*

window=Tk()
window.title("Hello")
def button_click():
    print("Button clicked")

button=Button(window,text="Click here",command=button_click)
button.pack(padx=20,pady=20)
window.mainloop()'''

from tkinter import*

window=Tk()
window.title("Hello")
def button_click():
    button.config(text="Good Job",bg="red",fg="black")

button=Button(window,text="Click here",command=button_click)
button.pack(padx=200,pady=200)
window.mainloop()