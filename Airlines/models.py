from django.db import models

# Employee model
class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

# Flight Crew model
class FlightCrew(models.Model):
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    role = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.employee} ({self.role}) - {self.flight}"

# Airport model
class Airport(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Aircraft model
class Aircraft(models.Model):
    model = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.model

# Flight model
class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    departure_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departing_flights')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arriving_flights')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE)

    def __str__(self):
        return self.flight_number

# Passenger model
class Passenger(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    passport_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Booking model
class Booking(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking by {self.passenger} on {self.flight}"

# Payment model
class Payment(models.Model):
    ticket = models.OneToOneField('Ticket', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment for Ticket {self.ticket.id} - ${self.amount}"

# Ticket model
class Ticket(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)

    def __str__(self):
        return f"Ticket {self.id} - Seat {self.seat_number}"

class Route(models.Model):
    departure_airport = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='departure_routes')
    arrival_airport = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='arrival_routes')
    distance = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.departure_airport} → {self.arrival_airport} ({self.distance} km)"
    
class Schedule(models.Model):
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def __str__(self):
        return f"{self.flight} | {self.departure_time} → {self.arrival_time}"

