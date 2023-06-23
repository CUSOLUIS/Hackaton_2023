import tkinter as tk
from tkinter import ttk
from tkinter import *

key = tk.Tk()

key.title('Teclado Prueba')

key.geometry('870x250')

key.configure(bg= 'grey')

equation = tk.StringVar()
Dis_entry = ttk.Entry(key,state= 'readonly', textvariable=equation)
Dis_entry.grid(rowspan=1,columnspan=100, ipadx=999, ipady=10)

#marco = Frame(key, width=480,height=320)
#marco.pack()

q = ttk.Button(key, text='Q', width=6, command=lambda:press('Q'))
q.grid(row = 1, column = 0, ipadx = 6, ipady= 10)


exp = ' '

def clear():
    global exp
    exp = ' '
    equation.set(exp)

def press(num):
    global exp
    exp = exp + str(num)
    equation.set(exp)

def atras():
    global exp
    exp.destroy()
    equation.deiconify()

q = ttk.Button(key, text='Q', width=6, command=lambda:press('Q'))
q.grid(row = 1, column = 0, ipadx = 6, ipady= 10)

w = ttk.Button(key, text='W', width=6, command=lambda:press('W'))
w.grid(row = 1, column = 1, ipadx = 6, ipady= 10)

e = ttk.Button(key, text='E', width=6, command=lambda:press('E'))
e.grid(row = 1, column = 2, ipadx = 6, ipady= 10)

r = ttk.Button(key, text='R', width=6, command=lambda:press('R'))
r.grid(row = 1, column = 3, ipadx = 6, ipady= 10)

t = ttk.Button(key, text='T', width=6, command=lambda:press('T'))
t.grid(row = 1, column = 4, ipadx = 6, ipady= 10)

y = ttk.Button(key, text='Y', width=6, command=lambda:press('Y'))
y.grid(row = 1, column = 5, ipadx = 6, ipady= 10)

u = ttk.Button(key, text='U', width=6, command=lambda:press('U'))
u.grid(row = 1, column = 6, ipadx = 6, ipady= 10)

i = ttk.Button(key, text='I', width=6, command=lambda:press('I'))
i.grid(row = 1, column = 7, ipadx = 6, ipady= 10)

p = ttk.Button(key, text='P', width=6, command=lambda:press('P'))
p.grid(row = 1, column = 8, ipadx = 6, ipady= 10)


clear = ttk.Button(key, text='Clear', width=6, command=clear)
clear.grid(row = 1, column = 9, ipadx = 6, ipady= 10)
# 2da fila


a = ttk.Button(key, text='A', width=6, command=lambda:press('A'))
a.grid(row = 2, column = 0, ipadx = 6, ipady= 10)

s = ttk.Button(key, text='S', width=6, command=lambda:press('S'))
s.grid(row = 2, column = 1, ipadx = 6, ipady= 10)

d = ttk.Button(key, text='D', width=6, command=lambda:press('D'))
d.grid(row = 2, column = 2, ipadx = 6, ipady= 10)

f = ttk.Button(key, text='F', width=6, command=lambda:press('F'))
f.grid(row = 2, column = 3, ipadx = 6, ipady= 10)

g = ttk.Button(key, text='G', width=6, command=lambda:press('G'))
g.grid(row = 2, column = 4, ipadx = 6, ipady= 10)

h = ttk.Button(key, text='H', width=6, command=lambda:press('H'))
h.grid(row = 2, column = 5, ipadx = 6, ipady= 10)

j = ttk.Button(key, text='J', width=6, command=lambda:press('J'))
j.grid(row = 2, column = 6, ipadx = 6, ipady= 10)

k = ttk.Button(key, text='K', width=6, command=lambda:press('K'))
k.grid(row = 2, column = 7, ipadx = 6, ipady= 10)

l = ttk.Button(key, text='L', width=6, command=lambda:press('L'))
l.grid(row = 2, column = 8, ipadx = 6, ipady= 10)


#3ra Fila

z = ttk.Button(key, text='Z', width=6, command=lambda:press('Z'))
z.grid(row = 3, column = 0, ipadx = 6, ipady= 10)

x = ttk.Button(key, text='X', width=6, command=lambda:press('X'))
x.grid(row = 3, column = 1, ipadx = 6, ipady= 10)

c = ttk.Button(key, text='C', width=6, command=lambda:press('C'))
c.grid(row = 3, column = 2, ipadx = 6, ipady= 10)

v = ttk.Button(key, text='V', width=6, command=lambda:press('V'))
v.grid(row = 3, column = 3, ipadx = 6, ipady= 10)

b = ttk.Button(key, text='B', width=6, command=lambda:press('B'))
b.grid(row = 3, column = 3, ipadx = 6, ipady= 10)

n = ttk.Button(key, text='N', width=6, command=lambda:press('N'))
n.grid(row = 3, column = 3, ipadx = 6, ipady= 10)

m = ttk.Button(key, text='M', width=6, command=lambda:press('M'))
m.grid(row = 3, column = 4, ipadx = 6, ipady= 10)

space = ttk.Button(key, text='Space', width=80, command=lambda:press(' '))
space.grid(row =4, columnspan = 5, ipadx = 6, ipady= 10)



key.mainloop()