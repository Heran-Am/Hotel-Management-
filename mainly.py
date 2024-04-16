import tkinter as tk
from subprocess import call

def click_checkinn():
    call(["python", "checkin_gui_and_program.py"])

def click_list():
    call(["python", "listgui.py"])

def click_checkout():
    call(["python", "checkoutgui.py"])

def click_getinfo():
    call(["python", "getinfoui.py"])

class HotelManagementApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("963x749+540+110")
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

        welcome_message = tk.Message(frame, text='''WELCOME''', background="#d9d9d9", font=("Segoe UI", 40, "bold"))
        welcome_message.place(relx=0.09, rely=0.01, relheight=0.15, relwidth=0.86)

        buttons = [
            ("CHECK INN", click_checkinn),
            ("SHOW GUEST LIST", click_list),
            ("CHECK OUT", click_checkout),
            ("GET INFO OF ANY GUEST", click_getinfo),
            ("EXIT", quit)
        ]

        for index, (text, command) in enumerate(buttons, start=2):
            button = tk.Button(frame, text=text, background="#d9d9d9", font=("Segoe UI", 15, "bold"), command=command)
            button.place(relx=0.18, rely=0.16 + (index - 1) * 0.14, height=93, width=566)

if __name__ == '__main__':
    app = HotelManagementApp()
    app.root.mainloop()
