from django import forms
from .models import Booking, Passenger, Payment,Employee, FlightCrew, Airport, Aircraft, Flight, Ticket, Route, Schedule
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2'] 

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['passenger', 'flight']

class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['first_name', 'last_name', 'passport_number']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['ticket', 'amount', 'payment_method']

# Employee Form
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'position', 'salary']

# FlightCrew Form
class FlightCrewForm(forms.ModelForm):
    class Meta:
        model = FlightCrew
        fields = ['flight', 'employee', 'role']

# Airport Form
class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ['name', 'location']

# Aircraft Form
class AircraftForm(forms.ModelForm):
    class Meta:
        model = Aircraft
        fields = ['model', 'capacity']

# Flight Form
class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['flight_number', 'departure_airport', 'arrival_airport', 'departure_time', 'arrival_time', 'aircraft']

# Ticket Form
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['flight', 'seat_number']

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['departure_airport', 'arrival_airport', 'distance']

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['flight', 'departure_time', 'arrival_time']


