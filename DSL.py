class HotelDataHandler:
    @staticmethod
    def save_guest_data(guest_data):
        try:
            with open("hotel.dat", "ab") as f:
                pickle.dump(guest_data, f)
        except FileNotFoundError:
            print("Error: hotel.dat file not found.")

    @staticmethod
    def load_guest_data():
        guest_data = []
        try:
            with open("hotel.dat", "rb") as f:
                while True:
                    try:
                        guest = pickle.load(f)
                        guest_data.append(guest)
                    except EOFError:
                        break
        except FileNotFoundError:
            print("Error: hotel.dat file not found.")
        return guest_data

    @staticmethod
    def save_receipt_data(receipt_data):
        try:
            with open("receipt.txt", "w") as f:
                for line in receipt_data:
                    f.write(line + '\n')
        except FileNotFoundError:
            print("Error: receipt.txt file not found.")

    @staticmethod
    def load_receipt_data():
        receipt_data = []
        try:
            with open("receipt.txt", "r") as f:
                receipt_data = f.readlines()
        except FileNotFoundError:
            print("Error: receipt.txt file not found.")
        return receipt_data
