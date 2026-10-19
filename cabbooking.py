import random

def cab_booking_chatbot():
    # Predefined routes: source, destination, distance
    routes = {
        1: ("Pune Station", "Shivajinagar", 5),
        2: ("Swargate", "Kothrud", 8),
        3: ("Hinjawadi", "Wakad", 10)
    }

    # Cab rates per kilometre
    cab_rates = {
        1: ("Auto", 12),
        2: ("Sedan", 18),
        3: ("SUV", 25)
    }

    while True:
        print("\n========== CAB BOOKING CHATBOT ==========")
        print("1. Book Ride")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Select cab type
            print("\nChoose Cab Type:")
            for key, value in cab_rates.items():
                print(f"{key}. {value[0]} - Rs.{value[1]}/km")

            cab_choice = input("Enter cab choice (1-3): ")

            if cab_choice not in ("1", "2", "3"):
                print("Invalid cab choice. Please try again.")
                continue

            cab_choice = int(cab_choice)
            cab_name, rate = cab_rates[cab_choice]

            # Select route
            print("\nAvailable Routes:")
            for key, value in routes.items():
                print(
                    f"{key}. {value[0]} to {value[1]} "
                    f"- {value[2]} km"
                )

            route_choice = input("Enter route number (1-3): ")

            if route_choice not in ("1", "2", "3"):
                print("Invalid route choice. Please try again.")
                continue

            route_choice = int(route_choice)
            source, destination, distance = routes[route_choice]

            # Calculate fare
            fare = distance * rate

            print("\n========== BOOKING DETAILS ==========")
            print("Cab Type:", cab_name)
            print("Source:", source)
            print("Destination:", destination)
            print("Distance:", distance, "km")
            print("Rate: Rs.", rate, "/km")
            print("Total Fare: Rs.", fare)

            # Cancellation before OTP
            print("\n1. Confirm and Share OTP")
            print("2. Cancel Ride")

            confirm = input("Enter your choice: ")

            if confirm == "2":
                print("Ride cancelled successfully.")
                print("No OTP has been shared.")
                continue

            elif confirm != "1":
                print("Invalid choice. Returning to main menu.")
                continue

            # Generate and share 4-digit OTP
            otp = random.randint(1000, 9999)

            print("\nRide confirmed successfully!")
            print("Your 4-digit OTP is:", otp)
            print("OTP shared with the user.")

            # Cancellation is locked after OTP sharing
            print("Cancellation is now locked.")
            print("Please complete your ride.")

        elif choice == "2":
            print("\nThank you for using Cab Booking Chatbot!")
            print("Goodbye!")
            break

        else:
            print("Invalid menu choice. Please enter 1 or 2.")


# Start the chatbot
cab_booking_chatbot()