import os
import pickle

class Guest:
    def __init__(self):
        self.name = ""
        self.address = ""
        self.mobile_no = ""
        self.no_of_days = 0
        self.price = 0
        self.room = ""

    def enter(self):
        self.name = input("ENTER GUEST NAME: ")
        while not self.name.strip():
            print("Invalid input. Please input a valid name.")
            self.name = input("ENTER GUEST NAME: ")

        self.address = input("ENTER GUEST ADDRESS: ")
        while not self.address.strip():
            print("Invalid input. Please input a valid address.")
            self.address = input("ENTER GUEST ADDRESS: ")

        self.mobile_no = input("ENTER MOBILE/PHONE NO.: ")
        while not self.mobile_no.isdigit() or len(self.mobile_no) != 10:
            print("Invalid input. Please input a valid 10-digit mobile/phone number.")
            self.mobile_no = input("ENTER MOBILE/PHONE NO.: ")

        self.no_of_days = int(input("ENTER NO. OF DAYS GUEST WANT TO STAY: "))
        while self.no_of_days <= 0:
            print("Invalid input. Number of days must be greater than 0.")
            self.no_of_days = int(input("ENTER NO. OF DAYS GUEST WANT TO STAY: "))

    def choose_room(self):
        print("1. Delux")
        print("2. Semi-Delux")
        print("3.

