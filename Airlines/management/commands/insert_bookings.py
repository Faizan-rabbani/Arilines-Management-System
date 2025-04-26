from django.core.management.base import BaseCommand
from Airlines.models import Passenger, Flight, Booking, Route, Airport, Aircraft, Ticket, Payment  # Import necessary models
from decimal import Decimal
import random
from datetime import datetime

class Command(BaseCommand):
    help = 'Insert flight, airports, aircraft, route, 40 passengers, bookings, tickets, and payments for the flight'

    def handle(self, *args, **kwargs):
        # Step 1: Create Airports
        # Create Departure Airport (Los Angeles International Airport)
        lax, created = Airport.objects.get_or_create(
            name="Los Angeles International Airport (LAX)",
            location="Los Angeles, USA"
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Airport {lax.name} created successfully."))
        else:
            self.stdout.write(self.style.SUCCESS(f"Airport {lax.name} already exists."))

        # Create Arrival Airport (Heathrow Airport)
        lhr, created = Airport.objects.get_or_create(
            name="Heathrow Airport (LHR)",
            location="London, UK"
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Airport {lhr.name} created successfully."))
        else:
            self.stdout.write(self.style.SUCCESS(f"Airport {lhr.name} already exists."))

        # Step 2: Create Aircraft
        aircraft, created = Aircraft.objects.get_or_create(
            model="Boeing 777-300ER",
            capacity=396
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Aircraft {aircraft.model} created successfully."))
        else:
            self.stdout.write(self.style.SUCCESS(f"Aircraft {aircraft.model} already exists."))

        # Step 3: Create Flight (LA456)
        flight, created = Flight.objects.get_or_create(
            flight_number="LA456",
            departure_airport=lax,
            arrival_airport=lhr,
            departure_time="2024-12-26 16:00:00",
            arrival_time="2024-12-27 09:30:00",
            aircraft=aircraft
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Flight {flight.flight_number} created successfully."))
        else:
            self.stdout.write(self.style.SUCCESS(f"Flight {flight.flight_number} already exists."))

        # Step 4: Create Route (LAX → LHR)
        route, created = Route.objects.get_or_create(
            departure_airport=lax,
            arrival_airport=lhr,
            distance=1500
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f"Route from {lax.name} to {lhr.name} created successfully."))
        else:
            self.stdout.write(self.style.SUCCESS(f"Route from {lax.name} to {lhr.name} already exists."))

        # Step 5: Create 40 Passengers
        passengers_data = [
            ('Alex', 'Turner', 'P123456789'),
            ('Emma', 'Stone', 'P987654321'),
            ('Chris', 'Evans', 'P456789123'),
            ('Olivia', 'Wilde', 'P321654987'),
            ('Liam', 'Smith', 'P456123789'),
            ('Mia', 'Johnson', 'P654789321'),
            ('Noah', 'Brown', 'P321987654'),
            ('Ava', 'Davis', 'P123789456'),
            ('Isabella', 'Taylor', 'P654123789'),
            ('Ethan', 'Clark', 'P789654123'),
            ('Sophia', 'Martinez', 'P456789654'),
            ('Benjamin', 'Hernandez', 'P321456987'),
            ('Lily', 'Rodriguez', 'P654987321'),
            ('James', 'Garcia', 'P987321456'),
            ('Charlotte', 'Lee', 'P123654987'),
            ('Oliver', 'Young', 'P987654987'),
            ('Amelia', 'Allen', 'P456123456'),
            ('Lucas', 'King', 'P789123654'),
            ('Grace', 'Scott', 'P654321987'),
            ('Mason', 'Adams', 'P123987654'),
            ('Emily', 'Baker', 'P456987123'),
            ('Jacob', 'Nelson', 'P789321654'),
            ('Chloe', 'Carter', 'P321654123'),
            ('Michael', 'Mitchell', 'P654123456'),
            ('Isabella', 'Perez', 'P987654321'),
            ('Daniel', 'Roberts', 'P321123987'),
            ('Charlotte', 'Cooper', 'P654987654'),
            ('Jack', 'Campbell', 'P123654321'),
            ('Lily', 'Harris', 'P789456321'),
            ('Ethan', 'Thompson', 'P321456123'),
            ('Ava', 'Walker', 'P654321654'),
            ('Samuel', 'Edwards', 'P987321654'),
            ('Ella', 'Torres', 'P123987123'),
            ('Max', 'Rivera', 'P456654987'),
            ('Grace', 'Morris', 'P789654321'),
            ('William', 'Lee', 'P321987123'),
            ('Alexander', 'Walker', 'P654123789'),
            ('Mia', 'Scott', 'P987123654'),
            ('Daniel', 'Parker', 'P123456123'),
            ('Lily', 'Roberts', 'P654321456'),
        ]

        # Insert the 40 passengers
        for first_name, last_name, passport_number in passengers_data:
            passenger, created = Passenger.objects.get_or_create(
                first_name=first_name,
                last_name=last_name,
                passport_number=passport_number
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Passenger {passenger.first_name} {passenger.last_name} created successfully."))
            else:
                self.stdout.write(self.style.SUCCESS(f"Passenger {passenger.first_name} {passenger.last_name} already exists."))

        # Step 6: Insert bookings for 40 passengers
        passengers = Passenger.objects.all()[:40]  # Get the first 40 passengers
        for passenger in passengers:
            booking = Booking.objects.create(
                passenger=passenger,
                flight=flight
            )
            self.stdout.write(self.style.SUCCESS(f"Booking for {passenger.first_name} {passenger.last_name} created."))

            # Step 7: Create Tickets for each booking
            ticket = Ticket.objects.create(
                flight=flight,
                seat_number=f"{random.randint(1, 40)}{random.choice(['A', 'B', 'C', 'D', 'E', 'F'])}"
            )
            self.stdout.write(self.style.SUCCESS(f"Ticket {ticket.id} created for {passenger.first_name} {passenger.last_name}."))
            
            # Step 8: Create Payment for each ticket
            amount = Decimal(random.randint(300, 1500))  # Random amount for the ticket between $300 to $1500
            payment = Payment.objects.create(
                ticket=ticket,
                amount=amount,
                payment_date=datetime.now(),
                payment_method=random.choice(['Credit Card', 'PayPal', 'Bank Transfer'])
            )
            self.stdout.write(self.style.SUCCESS(f"Payment of ${payment.amount} created for Ticket {ticket.id}."))

        self.stdout.write(self.style.SUCCESS(f"Successfully inserted tickets and payments for 40 passengers on flight {flight.flight_number}."))
