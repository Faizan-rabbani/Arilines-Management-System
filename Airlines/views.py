from django.shortcuts import render, get_object_or_404, redirect
from .models import Flight, Booking, Passenger, Payment, Ticket, Employee, FlightCrew, Airport, Aircraft, Route, Schedule
from .forms import BookingForm, PassengerForm, PaymentForm, EmployeeForm, FlightCrewForm, AirportForm, AircraftForm, FlightForm, TicketForm, ScheduleForm, RouteForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm  # Import the custom form
from django.contrib.auth import update_session_auth_hash

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

# User login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index') 
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# User logout
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')  

def index(request):
    return render(request, 'index.html', {'flights': flights})


@login_required
def bookings(request):
    bookings = Booking.objects.all()
    return render(request, 'bookings.html', {'bookings': bookings})

def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_payment')
    else:
        form = BookingForm()
    return render(request, 'add_booking.html', {'form': form})

@login_required
def passengers(request):
    passengers = Passenger.objects.all()
    return render(request, 'passengers.html', {'passengers': passengers})

def add_passenger(request):
    if request.method == 'POST':
        form = PassengerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_booking')
    else:
        form = PassengerForm()
    return render(request, 'add_passenger.html', {'form': form})

@login_required
def employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})

def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EmployeeForm()
    return render(request, 'add_employee.html', {'form': form})

@login_required
def airports(request):
    airports = Airport.objects.all()
    return render(request, 'airports.html', {'airports': airports})

def add_airport(request):
    if request.method == 'POST':
        form = AirportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AirportForm()
    return render(request, 'add_airport.html', {'form': form})

@login_required
def aircrafts(request):
    aircrafts = Aircraft.objects.all()
    return render(request, 'aircrafts.html', {'aircrafts': aircrafts})

def add_aircraft(request):
    if request.method == 'POST':
        form = AircraftForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AircraftForm()
    return render(request, 'add_aircraft.html', {'form': form})

@login_required
def flights(request):
    flights = Flight.objects.all()
    return render(request, 'flights.html', {'flights': flights})

def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FlightForm()
    return render(request, 'add_flight.html', {'form': form})

@login_required
def payments_list(request):
    payments = Payment.objects.all()
    return render(request, 'payments.html', {'payments': payments})

def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PaymentForm()
    return render(request, 'add_payment.html', {'form': form})

@login_required
def flightcrew_list(request):
    crew_members = FlightCrew.objects.all()
    return render(request, 'flightcrew.html', {'crew_members': crew_members})

def add_flightcrew(request):
    if request.method == 'POST':
        form = FlightCrewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FlightCrewForm()
    return render(request, 'add_flightcrew.html', {'form': form})

@login_required
def routes_list(request):
    routes = Route.objects.all()
    return render(request, 'routes.html', {'routes': routes})

def add_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RouteForm()
    return render(request, 'add_route.html', {'form': form})

@login_required
def tickets_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'tickets.html', {'tickets': tickets})

def add_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TicketForm()
    return render(request, 'add_ticket.html', {'form': form})

@login_required
def schedules_list(request):
    schedules = Schedule.objects.all()
    return render(request, 'schedules.html', {'schedules': schedules})

def add_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ScheduleForm()
    return render(request, 'add_schedule.html', {'form': form})

# Edit and delete views for booking
def edit_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'edit_booking.html', {'form': form})

def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('dashboard')

# Similar edit and delete views for other models (Passenger, Employee, Flight, etc.)
def edit_passenger(request, passenger_id):
    passenger = get_object_or_404(Passenger, id=passenger_id)
    if request.method == 'POST':
        form = PassengerForm(request.POST, instance=passenger)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PassengerForm(instance=passenger)
    return render(request, 'edit_passenger.html', {'form': form})

def delete_passenger(request, passenger_id):
    passenger = get_object_or_404(Passenger, id=passenger_id)
    passenger.delete()
    return redirect('dashboard')


def edit_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form})

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return redirect('dashboard')


def edit_airport(request, airport_id):
    airport = get_object_or_404(Airport, id=airport_id)
    if request.method == 'POST':
        form = AirportForm(request.POST, instance=airport)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AirportForm(instance=airport)
    return render(request, 'edit_airport.html', {'form': form})

def delete_airport(request, airport_id):
    airport = get_object_or_404(Airport, id=airport_id)
    airport.delete()
    return redirect('dashboard')


def edit_aircraft(request, aircraft_id):
    aircraft = get_object_or_404(Aircraft, id=aircraft_id)
    if request.method == 'POST':
        form = AircraftForm(request.POST, instance=aircraft)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = AircraftForm(instance=aircraft)
    return render(request, 'edit_aircraft.html', {'form': form})

def delete_aircraft(request, aircraft_id):
    aircraft = get_object_or_404(Aircraft, id=aircraft_id)
    aircraft.delete()
    return redirect('dashboard')


def edit_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    if request.method == 'POST':
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FlightForm(instance=flight)
    return render(request, 'edit_flight.html', {'form': form})

def delete_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    flight.delete()
    return redirect('dashboard')


def edit_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST, instance=payment)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PaymentForm(instance=payment)
    return render(request, 'edit_payment.html', {'form': form})

def delete_payment(request, payment_id):
    payment = get_object_or_404(Payment, id=payment_id)
    payment.delete()
    return redirect('dashboard')


def edit_flightcrew(request, crew_id):
    crew = get_object_or_404(FlightCrew, id=crew_id)
    if request.method == 'POST':
        form = FlightCrewForm(request.POST, instance=crew)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = FlightCrewForm(instance=crew)
    return render(request, 'edit_flightcrew.html', {'form': form})

def delete_flightcrew(request, crew_id):
    crew = get_object_or_404(FlightCrew, id=crew_id)
    crew.delete()
    return redirect('dashboard')


def edit_route(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    if request.method == 'POST':
        form = RouteForm(request.POST, instance=route)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = RouteForm(instance=route)
    return render(request, 'edit_route.html', {'form': form})

def delete_route(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    route.delete()
    return redirect('dashboard')


def edit_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'edit_ticket.html', {'form': form})

def delete_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    ticket.delete()
    return redirect('dashboard')


def edit_schedule(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, 'edit_schedule.html', {'form': form})

def delete_schedule(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    schedule.delete()
    return redirect('dashboard')

def dashboard(request):
    # Fetch data from the database
    flights = Flight.objects.all()
    bookings = Booking.objects.all()
    aircrafts = Aircraft.objects.all()
    airports = Airport.objects.all()
    passengers = Passenger.objects.all()
    employees = Employee.objects.all()
    payments = Payment.objects.all()
    flight_crew = FlightCrew.objects.all()
    routes = Route.objects.all()
    tickets = Ticket.objects.all()
    schedules = Schedule.objects.all()

    # Pass the data to the template
    context = {
        'flights': flights,
        'bookings': bookings,
        'aircrafts': aircrafts,
        'airports': airports,
        'passengers': passengers,
        'employees': employees,
        'payments': payments,
        'flightcrews': flight_crew,
        'routes': routes,
        'tickets': tickets,
        'schedules': schedules,
    }
    return render(request, 'dashboard.html', context)


def profile(request):
    return render(request, 'profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Get the current user
        user = request.user

        # Update username if provided
        if username and username != user.username:
            user.username = username

        # Handle password change if a new password is provided
        if new_password:
            if new_password == confirm_password:
                user.set_password(new_password)  # Hash the new password
                update_session_auth_hash(request, user)  # Keep the user logged in after password change
                messages.success(request, 'Your password has been updated successfully!')
            else:
                messages.error(request, 'Passwords do not match.')
                return redirect('edit_profile')  # Stay on the same page if there is an error

        # Save the user object
        user.save()
        messages.success(request, 'Your profile has been updated successfully!')
        return redirect('profile')  # Redirect to the profile page after saving changes

    return render(request, 'edit_profile.html')