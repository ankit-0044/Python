from tkinter import Button, Tk, messagebox
from tkinter import *
root = Tk()
root.geometry('300x300')
num1 = Entry(root)
num1.grid(row = 1, column = 0)
num1.focus_set()
num2 = Entry(root)
num2.grid(row=1, column=1)
num2.focus_set()

def Add ():
    global num1
    global num2
    string1 = int(num1.get())
    string2 = int(num2.get())
    messagebox.showinfo("Addition", f'{string1} + {string2} is: {string1 + string2}')
def Sub():
    global num1
    global num2
    string1= int(num1.get())
    string2= int(num2.get())
    messagebox.showinfo("Subtraction", f'{string1}-{string2} is: {string1 - string2}')
def Mult():
    global num1
    global num2
    string1 = int(num1.get())
    string2 = int(num2.get())
    messagebox.showinfo("Multiplication", f'{string1}* {string2} is: {string1 * string2}')
def Div():
    global num1
    global num2
    string1 = int(num1.get())
    string2 = int(num2.get())
    messagebox.showinfo("Division",f'{string1} / {string2} is: {string1 / string2}')

button1 = Button(root, text= 'Add ', command=Add, bg='cyan',height=1, width=7)
button1.grid(row=2, column=0)
button2 = Button(root, text= 'Sub', command=Sub, bg='cyan', height=1, width=7)
button2.grid(row=3, column=0)
button3 = Button(root, text='Multi', command=Mult, bg ='cyan', height=1, width=7)
button3.grid(row=4, column=0)
button4 = Button(root, text='Div', command=Div, bg='cyan',height=1, width=7)
button4.grid(row=5, column=0)
root.mainloop()