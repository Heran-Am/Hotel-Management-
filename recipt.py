#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import tkinter as tk

try:
    from tkinter import *
    # Import only needed names or import the module and then use its members.
except ImportError:
    from tkinter import *

class Receipt:
    def __init__(self):
        with open("recipt.txt", "r") as fo1:
            list1 = fo1.readlines()
            del list1[1:6]
            list1[0] = list1[0][:-1]
            list1[1] = list1[1][:-1]
            list1[2] = list1[2][:-1]
            list1[3] = list1[3][:-1]
            list1[4] = list1[4][:-1]

            p = '''
            @@@@@@@@@@@  PROJECTWORLDS HOTEL AND RESORTS  @@@@@@@@@@@@@
            @@@@@@@@@@@@ BHILAI CHHATTISGARH@@@@@@@@@@@@@@
            @@@@@@@@@@ SERVING    GUEST   SINCE @@@@@@@@@@@@@@@@@
            @@@@@@@@@@@@@@@    ###2000###       @@@@@@@@@@@@@@@@@
            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
            NAME-%s
            ADDRESS-%s
            MOBILE NO.-%s
            YOUR TOTAL BILL IS Rs.-%s
            YOUR ROOM NUMBER IS %s    

            ''' % (list1[0], list1[1], list1[2], list1[4], list1[3])

        root = tk.Tk()
        root.geometry("800x800")
        root.title("Receipt")
        root.configure(background="#d9d9d9")

        self.label = Label(root, background="#d9d9d9", text=p, disabledforeground="#a3a3a3", foreground="#000000",
                           anchor=N, wraplength=1000, justify=LEFT)
        self.label.place(relx=0, rely=0, height=800, width=800)

        root.mainloop()

if __name__ == '__main__':
    recipt1 = Receipt()
