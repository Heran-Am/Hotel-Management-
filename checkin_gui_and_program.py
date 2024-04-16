import os
import pickle
import sys
from subprocess import call

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

details_list = []


class save:
    def __init__(self, NAME_PRO, ADDRESS_PRO, MOBILE_NO_PRO, ROOM_NO_PRO, PRICE_PRO):
        self.name = NAME_PRO
        self.address = ADDRESS_PRO
        self.mobile_no = MOBILE_NO_PRO
        self.room_no = ROOM_NO_PRO
        self.price = PRICE_PRO


class HOTEL_MANGMENT_checkin:
    def __init__(self):
        self.NAME = ""
        self.ADDRESS = ""
        self.MOBILE = ""
        self.DAYS = 0
        self.price = 0
        self.room = 0

    def chk_name(self):
        while True:
            self.k = str(self.name.get())
            a = self.k.isdigit()
            if len(self.k) != 0 and a != True:
                self.NAME = self.k
                self.Text1.insert(INSERT, "name has been inputted" + "\n")
                break
            else:
                self.Text1.insert(INSERT, "invalid input please input a valid name" + "\n")
                break

    def chk_add(self):
        while True:
            self.g = str(self.addr.get())
            ak = self.g.isdigit()
            if len(self.g) != 0 and ak != True:
                self.ADDRESS = self.g
                self.Text1.insert(INSERT, "address has been inputted" + "\n")
                break
            else:
                self.Text1.insert(INSERT, "invalid input please input a valid address" + "\n")
                break

    def chk_mo(self):
        while True:
            self.h = str(self.mobile.get())
            if self.h.isdigit() == True and len(self.h) != 0 and len(self.h) == 10:
                self.MOBILE = self.h
                self.Text1.insert(INSERT, "mobile number has been inputted" + "\n")
                break
            else:
                self.Text1.insert(INSERT, "invalid input please input a valid mobile number" + "\n")
                break

    def chk_day(self):
        while True:
            self.l = str(self.days.get())
            if self.l.isdigit() == True and len(self.l) != 0:
                self.DAYS = int(self.l)
                self.Text1.insert(INSERT, "days has been inputted" + "\n")
                break
            else:
                self.Text1.insert(INSERT, "invalid input " + "\n")
                break

    def enter(self):
        self.name = self.NAME
        self.address = self.ADDRESS
        self.mobile_no = self.MOBILE
        self.no_of_days = int(self.DAYS)

    def tor(self):
        if self.ch == 1:
            self.price = self.price + (2000 * self.no_of_days)
            m[0] = 1
        elif self.ch == 2:
            self.price = self.price + (1500 * self.no_of_days)
            m[0] = 2
        elif self.ch == 3:
            self.price = self.price + (1000 * self.no_of_days)
            m[0] = 3
        elif self.ch == 4:
            self.price = self.price + (1700 * self.no_of_days)
            m[0] = 4

    def payment_option(self):
        op = self.p
        if op == 1:
           
