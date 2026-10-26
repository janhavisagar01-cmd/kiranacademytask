from abc import ABC, abstractmethod


# 1. Abstract Base Class: Passenger
class Passenger(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_discount(self):
        pass

    @abstractmethod
    def get_passenger_type(self):
        pass


# 2. Inheritance: Regular Passenger
class RegularPassenger(Passenger):
    def get_discount(self):
        return 0.0

    def get_passenger_type(self):
        return "Regular"


# 3. Inheritance: Student Passenger
class StudentPassenger(Passenger):
    def get_discount(self):
        return 0.10

    def get_passenger_type(self):
        return "Student"


# 4. Flight Class
class Flight:
    def __init__(self, code, airline, source, destination,
                 available_seats, base_fare):
        self.code = code
        self.airline = airline
        self.source = source
        self.destination = destination
        self._available_seats = available_seats
        self.base_fare = base_fare

    @property
    def available_seats(self):
        return self._available_seats

    def display_flight(self):
        print(
            f"{self.code:<10} {self.airline:<15} "
            f"{self.source:<12} {self.destination:<12} "
            f"{self.available_seats:<8} Rs.{self.base_fare}"
        )

    def has_enough_seats(self, tickets):
        return tickets <= self._available_seats

    def reserve_seats(self, tickets):
        if self.has_enough_seats(tickets):
            self._available_seats -= tickets
            return True
        return False


# 5. Booking Class
class Booking:
    def __init__(self, booking_id, flight, passenger, tickets):
        self.booking_id = booking_id
        self.flight = flight
        self.passenger = passenger
        self.tickets = tickets

        self.subtotal = flight.base_fare * tickets
        self.discount = self.subtotal * passenger.get_discount()
        self.total_fare = self.subtotal - self.discount

    def display_summary(self):
        print("\n========== BOOKING SUMMARY ==========")
        print(f"Booking ID          : {self.booking_id}")
        print(f"Flight Code         : {self.flight.code}")
        print(f"Airline             : {self.flight.airline}")
        print(f"Route               : {self.flight.source} to "
              f"{self.flight.destination}")
        print(f"Passenger Name      : {self.passenger.name}")
        print(f"Passenger Age       : {self.passenger.age}")
        print(f"Passenger Type      : "
              f"{self.passenger.get_passenger_type()}")
        print(f"Number of Tickets   : {self.tickets}")
        print(f"Base Fare Per Ticket: Rs.{self.flight.base_fare:.2f}")
        print(f"Subtotal            : Rs.{self.subtotal:.2f}")
        print(f"Discount            : Rs.{self.discount:.2f}")
        print(f"Final Amount        : Rs.{self.total_fare:.2f}")
        print("=====================================")


# 6. Flight Booking System Class
class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("PN101", "Air India", "Pune", "Delhi", 20, 4000),
            Flight("MB102", "IndiGo", "Mumbai", "Bengaluru", 30, 3500),
            Flight("PN103", "SpiceJet", "Pune", "Hyderabad", 25, 3000)
        ]

        self.bookings = []
        self.booking_counter = 1001

    # Display all available flights
    def display_flights(self):
        print("\n================ AVAILABLE FLIGHTS ================")
        print(
            f"{'Code':<10} {'Airline':<15} {'Source':<12} "
            f"{'Destination':<12} {'Seats':<8} {'Base Fare'}"
        )
        print("-" * 75)

        for flight in self.flights:
            flight.display_flight()

        print("=" * 75)

    # Find flight using flight code
    def find_flight(self, flight_code):
        for flight in self.flights:
            if flight.code.lower() == flight_code.lower():
                return flight
        return None

    # Validate booking details
    def validate_booking(self, flight, name, age, tickets):
        if flight is None:
            print("Error: Invalid flight code.")
            return False

        if not name.strip():
            print("Error: Passenger name cannot be blank.")
            return False

        if age <= 0:
            print("Error: Age must be greater than zero.")
            return False

        if tickets <= 0:
            print("Error: Number of tickets must be greater than zero.")
            return False

        if not flight.has_enough_seats(tickets):
            print("Booking failed: Not enough seats available.")
            return False

        return True

    # Book a flight
    def book_flight(self):
        print("\n========== BOOK A FLIGHT ==========")

        flight_code = input("Enter flight code: ").strip()
        flight = self.find_flight(flight_code)

        if flight is None:
            print("Error: Flight code not found.")
            return

        name = input("Enter passenger name: ").strip()

        try:
            age = int(input("Enter passenger age: "))
            if age <= 0:
                print("Error: Age must be greater than zero.")
                return

            passenger_type = input(
                "Passenger type (Regular/Student): "
            ).strip().lower()

            if passenger_type not in ("regular", "student"):
                print("Error: Choose Regular or Student.")
                return

            tickets = int(input("Enter number of tickets: "))

        except ValueError:
            print("Error: Age and ticket count must be valid integers.")
            return

        # Validate every booking detail before making a reservation
        if not self.validate_booking(flight, name, age, tickets):
            return

        # Create the appropriate passenger object
        if passenger_type == "student":
            passenger = StudentPassenger(name, age)
        else:
            passenger = RegularPassenger(name, age)

        # Create booking and calculate fare
        booking_id = f"BK{self.booking_counter}"
        booking = Booking(booking_id, flight, passenger, tickets)

        # Update seats only after successful validation
        if flight.reserve_seats(tickets):
            self.bookings.append(booking)
            self.booking_counter += 1

            print("\nBooking confirmed successfully!")
            booking.display_summary()
        else:
            print("Booking failed: Not enough seats available.")

    # Display the latest confirmed booking
    def view_booking(self):
        if not self.bookings:
            print("\nNo bookings available yet.")
            return

        print("\nMost Recent Confirmed Booking:")
        self.bookings[-1].display_summary()

    # Main menu
    def run(self):
        print("\nWelcome to Kiran Air Booking!")

        while True:
            print("\n========== MAIN MENU ==========")
            print("1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.display_flights()

            elif choice == "2":
                self.book_flight()

            elif choice == "3":
                self.view_booking()

            elif choice == "4":
                print("\nThank you for using Kiran Air Booking!")
                print("Have a safe journey!")
                break

            else:
                print("Invalid choice. Please select 1, 2, 3, or 4.")


# 7. Main Program
if __name__ == "__main__":
    system = FlightBookingSystem()
    system.run()