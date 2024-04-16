import os
import pickle
import sys
from tkinter import *
from tkinter import messagebox

class Guest:
    def __init__(self, name, address, mobile_no, room_no, price):
        self.name = name
        self.address = address
        self.mobile_no = mobile_no
        self.room_no = room_no
        self.price = price

class HotelManagementApp:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("881x582+249+104")
        self.root.title("HOTEL MANAGEMENT")
        self.root.configure(background="#d9d9d9")
        self.setup_gui()

    def setup_gui(self):
        frame = Frame(self.root)
        frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.94)
        frame.configure(relief=GROOVE)
        frame.configure(borderwidth="2")
        frame.configure(relief=GROOVE)
        frame.configure(background="#d9d9d9")
        frame.configure(width=825)

        self.text_area = Text(frame)
        self.text_area.place(relx=0.04, rely=0.46, relheight=0.48, relwidth=0.93)
        self.text_area.configure(background="white")
        self.text_area.configure(font="TkTextFont")
        self.text_area.configure(foreground="black")
        self.text_area.configure(highlightbackground="#d9d9d9")
        self.text_area.configure(highlightcolor="black")
        self.text_area.configure(insertbackground="black")
        self.text_area.configure(selectbackground="#c4c4c4")
        self.text_area.configure(selectforeground="black")
        self.text_area.configure(width=764)

        label = Label(frame, text="ENTER THE ROOM NO.   :", background="#d9d9d9", font=("Segoe UI", 23, "bold"))
        label.place(relx=0.12, rely=0.15, height=48, width=377)

        self.room_entry = Entry(frame)
        self.room_entry.place(relx=0.65, rely=0.17, height=40, relwidth=0.1)
        self.room_entry.configure(background="white")
        self.room_entry.configure(font="TkFixedFont")
        self.room_entry.configure(foreground="#000000")
        self.room_entry.configure(insertbackground="black")
        self.room_entry.configure(width=84)

        submit_button = Button(frame, text="SUBMIT", background="#d9d9d9", font=("Segoe UI", 17, "bold"), command=self.get_info)
        submit_button.place(relx=0.39, rely=0.29, height=74, width=197)

        message = Message(frame, text="GET INFO HERE ..!!", background="#d9d9d9", font=("Segoe UI", 28, "bold"))
        message.place(relx=0.22, rely=0.02, relheight=0.12, relwidth=0.56)

    def get_info(self):
        room_number = self.room_entry.get()
        if room_number.isdigit() and len(room_number) != 0:
            self.text_area.insert(INSERT, "Valid room number\n")
            self.show_guest_info(room_number)
        else:
            self.text_area.insert(INSERT, "Invalid room number\n")

    def show_guest_info(self, room_number):
        try:
            with open("hotel.dat", "rb") as f:
                found = False
                while True:
                    guest = pickle.load(f)
                    if guest.room_no == room_number:
                        found = True
                        self.display_guest_details(guest)
                        break
        except FileNotFoundError:
            messagebox.showerror("File Error", "hotel.dat file not found.")
        except EOFError:
            pass
        if not found:
            self.text_area.insert(INSERT, f"No guest found in room {room_number}\n")

    def display_guest_details(self, guest):
        self.text_area.insert(INSERT, f"NAME: {guest.name}\n")
        self.text_area.insert(INSERT, f"ADDRESS: {guest.address}\n")
        self.text_area.insert(INSERT, f"MOBILE NO.: {guest.mobile_no}\n")
        self.text_area.insert(INSERT, f"HIS TOTAL BILL IS Rs. {guest.price}\n")
        self.text_area.insert(INSERT, "----------------------------------------\n")

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    app = HotelManagementApp()
    app.run()
