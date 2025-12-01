print("Welcome to Ticket Booking System ")
age = int(input("Enter your age: "))
if age < 20:
    print("Booking Rejected: You must be 14+ to book a ticket.")
elif 20 <= age <= 25:
    consent = input("Do you have parent consent? (yes/no): ")
    if consent == "yes":
        print("Booking Successful! Parent consent verified.")
    else:
        print("Booking Rejected: Parent consent required for ages 14–18.")
else:
    print("You are eligible to book a ticket.")
    partner = input("Are you with a partner? (yes/no): ").lower()
    if partner == "yes":
        print("""
You can choose:
1. Normal Seat
2. Couple Seat
        """)
        choice = input("Enter your choice: ")
        if choice == "1":
            print("✔ Normal Seat Booked!")
        elif choice == "2":
            print("Couple Seat Booked! Enjoy your time.")
        else:
            print("Invalid choice. Booking cancelled.")
    else:
        print("Normal Seat Booked!")
