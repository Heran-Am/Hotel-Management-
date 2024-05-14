import tkinter as tk
from tkinter import messagebox

class HotelManagementApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("881x582+249+104")
        self.root.title("HOTEL MANAGEMENT")
        self.root.configure(background="#d9d9d9")
        self.setup_gui()

    def setup_gui(self):
        frame = tk.Frame(self.root)
        frame.place(relx=0.02, rely=0.03, relheight=0.94, relwidth=0.96)
        frame.configure(relief=tk.GROOVE)
        frame.configure(borderwidth="2")
        frame.configure(relief=tk.GROOVE)
        frame.configure(background="#d9d9d9")
        frame.configure(highlightbackground="#d9d9d9")
        frame.configure(highlightcolor="black")
        frame.configure(width=925)
        pass

if __name__ == '__main__':
    app = HotelManagementApp()
    app.root.mainloop()
