#! python3
""" 
Create a binary converter.
Recall that binary is a system of counting based on powers of 2.
00000001 = 1
00000010 = 2
00001110 = 14

Create a converter that will convert binary to decimal or decimal to
binary using the interface shown in task1.png.  Use the shell that
has been started in task1.py
This is an incomplete program.  You will need to add onto it, 
but you should not change any of the commands that are already 
here

Use assignment_test.py to test your functions
"""

import tkinter as tk
from tkinter import *


def binary_to_decimal(binary):
    # binary is a tuple of length 8
    # return value is an integer decimal

    numbers = binary[0] + binary[1] + binary[2] + binary[3] + \
        binary[4] + binary[5] + binary[6] + binary[7]
    decimal = int(numbers, 2)
    return decimal


def decimal_to_binary(decimal):
    # decimal is an integer value
    # binary is a tuple of length 8 that contains 1's and 0's

    y = bin(decimal)[2:].zfill(8)
    binary = [y[0], y[1], y[2], y[3], y[4], y[5], y[6], y[7]]
    return binary


def get_binary():
    # function should read the entry widget and generate an integer
    # this integer will be used as an input parameter for decimal to binary and the result updated
    # in the 8 checkboxes
    decimal = int(e1.get())

    binary = decimal_to_binary(decimal)

    v1.set(binary[0])
    v2.set(binary[1])
    v3.set(binary[2])
    v4.set(binary[3])
    v5.set(binary[4])
    v6.set(binary[5])
    v7.set(binary[6])
    v8.set(binary[7])


def get_decimal():
    # function should read the checkboxes and generate a tuple called binary of length 8 that has 1's and 0's
    # this tuple will be used as an input parameter for binary_to_decimal and the result updated
    # in the entry box
    x1 = str(v1.get())
    x2 = str(v2.get())
    x3 = str(v3.get())
    x4 = str(v4.get())
    x5 = str(v5.get())
    x6 = str(v6.get())
    x7 = str(v7.get())
    x8 = str(v8.get())

    binary = [x1, x2, x3, x4, x5, x6, x7, x8]
    decimal = binary_to_decimal(binary)

    oBox.set(decimal)


win = tk.Tk()

v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
v5 = IntVar()
v6 = IntVar()
v7 = IntVar()
v8 = IntVar()

oBox = StringVar()
oBox.set("")

l1 = Label(win, text="Binary / Decimal Converter!")

cF = Frame()
c1 = Checkbutton(cF, onvalue=1, offvalue=0, variable=v1)
c2 = Checkbutton(cF, onvalue=1, offvalue=0, variable=v2)
c3 = Checkbutton(cF, onvalue=1, offvalue=0, variable=v3)
c4 = Checkbutton(cF, onvalue=1, offvalue=0, variable=v4)
c5 = Checkbutton(cF, onvalue=1, offvalue=0, variable=v5)
c6 = Checkbutton(cF, onvalue=1, offvalue=0, variable=v6)
c7 = Checkbutton(cF, onvalue=1, offvalue=0, variable=v7)
c8 = Checkbutton(cF, onvalue=1, offvalue=0, variable=v8)

bF = Frame()
b1 = Button(bF, text="Convert to Binary", command=get_binary)
b2 = Button(bF, text="Convert to Decimal", command=get_decimal)

e1 = Entry(win, textvariable=oBox)

l1.pack()

cF.pack()
c1.pack(side=LEFT)
c2.pack(side=LEFT)
c3.pack(side=LEFT)
c4.pack(side=LEFT)
c5.pack(side=LEFT)
c6.pack(side=LEFT)
c7.pack(side=LEFT)
c8.pack(side=LEFT)

bF.pack()
b1.pack(side=LEFT)
b2.pack(side=LEFT)

e1.pack()

win.mainloop()
