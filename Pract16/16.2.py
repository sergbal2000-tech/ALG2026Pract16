import tkinter as tk
from tkinter import messagebox

def add_dig(digit):
    value = calc.get()
    if value[0]=='0' and len(value)==1:
        value = value[1:]
    calc.delete (0, tk. END)
    calc.insert (0, value+digit)

def add_op(operation):
    value = calc.get()
    if value[-1] in '-+/*':
        value = value [:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk. END)
    calc.insert(0, value+operation)

def calculate():
    value = calc.get()
    if value[-1] in '-+/*':
        value = value+value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo("Внимание","Нужно вводить только цифры")
        calc.insert(0, eval(value))
    except ZeroDivisionError:
        messagebox.showinfo("Внимание", "На ноль делить нельзя")
        calc.insert(0, 0)

def clear():
    calc.delete(0, tk.END)
    calc.insert(0, 0)

def makedigitbutton(digit):
    return tk.Button(text=digit, bd=5,font=('Arial', 13), command=lambda: add_dig(digit))

def makeoperationbutton(operation):
    return tk.Button(text=operation, bd=5,font=('Arial', 13), command=lambda: add_op(operation))

def makecalcbutton(operation):
    return tk.Button(text=operation, bd=5,font=('Arial', 13), command=calculate)

def makeclearbutton(operation):
    return tk.Button(text=operation, bd=5,font=('Arial', 13), command=clear)

def presskey(event):
    if event.char.isdigit():
        add_dig(event.char)
    elif event.char in '+-/*':
        add_op(event.char)
    elif event.char == '\r':
        calculate()

win = tk.Tk()
win.geometry('240x570')
win['bg'] = '#33ffe6'
win.title('Калькулятор')

win.bind('<Key>',presskey)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert (0,'0')
calc.grid(row=0,column=0, columnspan=4, stick='we', padx=5)

makedigitbutton('1').grid(row=1,column=0,stick='wens',padx=5,pady=5)
makedigitbutton('2').grid(row=1,column=1,stick='wens',padx=5,pady=5)
makedigitbutton('3').grid(row=1,column=2,stick='wens',padx=5,pady=5)
makedigitbutton('4').grid(row=2,column=0,stick='wens',padx=5,pady=5)
makedigitbutton('5').grid(row=2,column=1,stick='wens',padx=5,pady=5)
makedigitbutton('6').grid(row=2,column=2,stick='wens',padx=5,pady=5)
makedigitbutton('7').grid(row=3,column=0,stick='wens',padx=5,pady=5)
makedigitbutton('8').grid(row=3,column=1,stick='wens',padx=5,pady=5)
makedigitbutton('9').grid(row=3,column=2,stick='wens',padx=5,pady=5)
makedigitbutton('0').grid(row=4,column=0,stick='wens',padx=5,pady=5)

makeoperationbutton('+').grid(row=1,column=3,stick='wens',padx=5,pady=5)
makeoperationbutton('-').grid(row=2,column=3,stick='wens',padx=5,pady=5)
makeoperationbutton('*').grid(row=3,column=3,stick='wens',padx=5,pady=5)
makeoperationbutton('/').grid(row=4,column=3,stick='wens',padx=5,pady=5)

makecalcbutton('=').grid(row=4,column=2,stick='wens',padx=5,pady=5)
makeclearbutton('c').grid(row=4,column=1,stick='wens',padx=5,pady=5)

win.grid_columnconfigure(0, weight=60)
win.grid_columnconfigure(1, weight=60)
win.grid_columnconfigure(2, weight=60)
win.grid_columnconfigure(3, weight=60)

win.grid_rowconfigure(1, weight=60)
win.grid_rowconfigure(2, weight=60)
win.grid_rowconfigure(3, weight=60)
win.grid_rowconfigure(4, weight=60)

win.mainloop()