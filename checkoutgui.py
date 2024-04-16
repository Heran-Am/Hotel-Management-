import pickle
import tkinter as tk
from tkinter import Text, INSERT, GROOVE, Frame, Entry, Button, Label

details_list = []
l2 = []
G = []

def file_save():
    NAME_PRO = details_list[0]
    ADDRESS_PRO = details_list[1]
    MOBILE_NO_PRO = details_list[2]
    ROOM_NO_PRO = details_list[3]
    PRICE_PRO = details_list[4]
    with open("hotel.dat", "ab") as f:
        a = (NAME_PRO, ADDRESS_PRO, MOBILE_NO_PRO, ROOM_NO_PRO, PRICE_PRO)
        pickle.dump(a, f, protocol=2)
    restart_program()

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

class New_Toplevel:
    def __init__(self):
        def check_room():
            rom = data.get()
            print(rom)
            print("\n")
            if rom.isdigit() and len(rom) != 0:
                text1.insert(INSERT, " valid room number ""\n")
                v = int(rom)
                with open("hotel.dat", "rb") as f, open("hote.dat", "ab") as f1:
                    n = 0
                    try:
                        while True:
                            s = pickle.load(f)
                            if s[3] == v:
                                n = 1
                                name1 = s[0]
                                print(" ")
                            else:
                                pickle.dump(s, f1)
                    except EOFError:
                        if n == 0:
                            text1.insert(INSERT, "NO GUEST FOUND""\n")
                        elif n == 1:
                            text1.insert(INSERT, "THANK YOU  " + name1.upper() + " FOR VISTING US""\n")
                        pass
                os.remove("hotel.dat")
                os.rename("hote.dat", "hotel.dat")
            else:
                text1.insert(INSERT, "invalid input please input a valid ROOM NO.""\n")

        root = tk.Tk()
        root.geometry("1011x750")
        root.title("HOTEL MANAGEMENT")
        root.configure(background="#ffffff")
        root.configure(highlightbackground="#ffffff")
        root.configure(highlightcolor="black")

        frame1 = Frame(root)
        frame1.place(relx=0.04, rely=0.04, relheight=0.91, relwidth=0.91)
        frame1.configure(relief=GROOVE)
        frame1.configure(borderwidth="2")
        frame1.configure(relief=GROOVE)
        frame1.configure(background="#ffffff")
        frame1.configure(highlightbackground="#ffffff")
        frame1.configure(highlightcolor="black")
        frame1.



if __name__ == '__main__':
    out=New_Toplevel()
