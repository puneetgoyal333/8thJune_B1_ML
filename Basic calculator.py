from tkinter import *
import tkinter as tk

app = tk.Tk()
app.title('Basic Calculator')
app.geometry('500x400')

equation = StringVar()

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


result = tk.Variable(app)
expression_field = Entry(app, textvariable=equation,
                         width=75).place(x=20, y=20)


tk.Button(app, text='7', width=5, height=2,
          command=lambda: press(7)).place(x=30, y=50)
tk.Button(app, text='8', width=5, height=2,
          command=lambda: press(8)).place(x=80, y=50)
tk.Button(app, text='9', width=5, height=2,
          command=lambda: press(9)).place(x=130, y=50)
tk.Button(app, text='/', width=5, height=2,
          command=lambda: press('/')).place(x=180, y=50)

tk.Button(app, text='4', width=5, height=2,
          command=lambda: press(4)).place(x=30, y=120)
tk.Button(app, text='5', width=5, height=2,
          command=lambda: press(5)).place(x=80, y=120)
tk.Button(app, text='6', width=5, height=2,
          command=lambda: press(6)).place(x=130, y=120)
tk.Button(app, text='*', width=5, height=2,
          command=lambda: press('*')).place(x=180, y=120)

tk.Button(app, text='1', width=5, height=2,
          command=lambda: press(1)).place(x=30, y=190)
tk.Button(app, text='2', width=5, height=2,
          command=lambda: press(2)).place(x=80, y=190)
tk.Button(app, text='3', width=5, height=2,
          command=lambda: press(3)).place(x=130, y=190)
tk.Button(app, text='-', width=5, height=2,
          command=lambda: press('-')).place(x=180, y=190)

tk.Button(app, text='C', width=5, height=2,
          command=lambda: clear()).place(x=30, y=260)
tk.Button(app, text='0', width=5, height=2,
          command=lambda: press(0)).place(x=80, y=260)
tk.Button(app, text='=', width=5, height=2,
          command=lambda: equalpress()).place(x=130, y=260)
tk.Button(app, text='+', width=5, height=2,
          command=lambda: press('+')).place(x=180, y=260)


app.mainloop()
