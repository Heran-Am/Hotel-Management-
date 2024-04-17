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
        print("3. General")
        print("4. Joint Room")
        while True:
            choice = input("Enter guest's choice: ")
            if choice.isdigit() and 1 <= int(choice) <= 4:
                break
            else:
                print("Invalid input. Please enter a valid choice (1-4).")
        choice = int(choice)

        if choice == 1:
            self.price += 2000 * self.no_of_days
            self.room = "Delux"
        elif choice == 2:
            self.price += 1500 * self.no_of_days
            self.room = "Semi-Delux"
        elif choice == 3:
            self.price += 1000 * self.no_of_days
            self.room = "General"
        elif choice == 4:
            self.price += 1700 * self.no_of_days
            self.room = "Joint Room"

    def payment_option(self):
        print("1. By cash")
        print("2. By credit/debit card")
        while True:
            option = input("Enter guest's payment option: ")
            if option.isdigit() and int(option) in [1, 2]:
                option = int(option)
                break
            else:
                print("Invalid input. Please enter a valid payment option (1-2).")

        if option == 2:
            self.price *= 0.9  # 10% discount for credit/debit card payment

    def generate_bill(self):
        print("\n@@@@@@@@@@@  5 STAR HOTEL   @@@@@@@@@@@@")
        print("@@@@ Asmara @@@@@@@")
        print("@@@ SERVING GUESTS SINCE 1991 @@@@")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("NAME:", self.name)
        print("ADDRESS:", self.address)
        print("MOBILE NO.:", self.mobile_no)
        print("ROOM TYPE:", self.room)
        print("NO. OF DAYS STAYED:", self.no_of_days)
        print("TOTAL BILL AMOUNT: Rs.", self.price)
        print("--------------------------------------------------")

def check_in():
    guest = Guest()
    guest.enter()
    guest.choose_room()
    guest.payment_option()
    guest.generate_bill()

    with open("hotel.dat", "ab") as f:
        pickle.dump(guest, f, protocol=2)

def show_guest_list():
    print("\nGUEST LIST:")
    print("NAME\t\tROOM TYPE")
    with open("hotel.dat", "rb") as f:
        try:
            while True:
                guest = pickle.load(f)
                print(f"{guest.name}\t\t{guest.room}")
        except EOFError:
            pass

def check_out():
    room_number = input("\nEnter ROOM NO.: ")
    temp_file = "temp.dat"

    with open("hotel.dat", "rb") as f, open(temp_file, "wb") as temp:
        guest_found = False
        try:
            while True:
                guest = pickle.load(f)
                if guest.room != room_number:
                    pickle.dump(guest, temp, protocol=2)
                else:
                    guest_found = True
        except EOFError:
            pass

    if guest_found:
        print("Guest checked out successfully.")
    else:
        print("No guest found in the specified room.")

    os.remove("hotel.dat")
    os.rename(temp_file, "hotel.dat")

def get_guest_info():
    room_number = input("\nEnter ROOM NO.: ")
    with open("hotel.dat", "rb") as f:
        guest_found = False
        try:
            while True:
                guest = pickle.load(f)
                if guest.room == room_number:
                    guest_found = True
                    guest.generate_bill()
        except EOFError:
            pass

    if not guest_found:
        print("No guest found in the specified room.")

def main():
    print(
        "///////////////****************//////////////*****************/////////////////*****************///////////////////******************//////////")
    print(
        "----------------------------------------------------- 5 STAR HOTEL  -----------------------------------------------------------------")
    print(
        "//////////////****************///////////////*****************/////////////////*****************///////////////////******************//////////")

    while True:
        print("\n1. Check in")
        print("2. Show guest list")
        print("3. Check out")
        print("4. Get info of any guest")
        print("5. EXIT")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_in()
        elif choice == "2":
            show_guest_list()
        elif choice == "3":
            check_out()
        elif choice == "4":
            get_guest_info()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try
