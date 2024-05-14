def filter_guests_by_room(room_number):
    """
    Filter guest data by room number.
    """
    guest_data = HotelDataHandler.load_guest_data()
    filtered_guests = filter(lambda guest: guest.room_no == room_number, guest_data)
    return list(filtered_guests)

def calculate_total_bill(guest_name):
    """
    Calculate the total bill for a guest.
    """
    guest_data = HotelDataHandler.load_guest_data()
    for guest in guest_data:
        if guest.name == guest_name:
            return guest.price
    return None

def generate_receipt(guest_name):
    """
    Generate a receipt for a guest.
    """
    guest_data = HotelDataHandler.load_guest_data()
    receipt_data = []
    for guest in guest_data:
        if guest.name == guest_name:
            receipt_data.append(f"NAME: {guest.name}")
            receipt_data.append(f"ADDRESS: {guest.address}")
            receipt_data.append(f"MOBILE NO.: {guest.mobile_no}")
            receipt_data.append(f"HIS TOTAL BILL IS Rs. {guest.price}")
            receipt_data.append(f"ROOM NUMBER: {guest.room_no}")
            break
    return receipt_data

def main():
    # Example usage
    room_number = "101"
    guests_in_room = filter_guests_by_room(room_number)
    print(f"Guests in room {room_number}:")
    for guest in guests_in_room:
        print(f"Name: {guest.name}, Room No: {guest.room_no}")

    guest_name = "John Doe"
    total_bill = calculate_total_bill(guest_name)
    if total_bill:
        print(f"Total bill for {guest_name}: Rs. {total_bill}")
    else:
        print(f"No guest found with name {guest_name}")

    receipt = generate_receipt(guest_name)
    if receipt:
        print("\nReceipt:")
        for line in receipt:
            print(line)

if __name__ == "__main__":
    main()
