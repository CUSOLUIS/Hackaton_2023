import tkinter as tk
from tkinter import *

class Window:
    def set(self):
        print("Hello World")
    def __init__(self, root):
        frame = Frame(root,bd = 5)
        first = Frame(root,bd = 5)
        second = Frame(root,bd = 5)
        third = Frame(root,bd = 5)
        buttonSize = 1
        Button(first, text="Q",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set(key),
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(first, text="W",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(first, text="E",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(first, text="R",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(first, text="T",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(first, text="Y",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(first, text="U",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(first, text="I",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(first, text="O",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(first, text="P",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        first.pack()

        Button(second, text="A",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(second, text="S",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(second, text="D",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(second, text="F",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(second, text="G",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(second, text="H",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(second, text="J",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(second, text="K",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(second, text="L",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(second, text="Ñ",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        second.pack()

        Button(third, text="Z",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(third, text="X",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(third, text="C",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(third, text="V",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(third, text="B",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(third, text="N",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(third, text="M",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(third, text="SPACE",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        Button(third, text="BACKSPACE",
               activebackground='#89908A', activeforeground='#89908A', bg='#c5cfc6', bd=2, command=set,
               font='console 14', highlightcolor='#89908A').pack(side=LEFT)
        third.pack()

root = tk.Tk()
root.update_idletasks()
root.attributes('-fullscreen', True)
root.state('iconic')
height = root.winfo_screenheight()
width = root.winfo_screenwidth()
root.geometry()
root.title("Keyboard")
display = Window(root)
root.mainloop()