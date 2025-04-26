from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    # Authentication URLs
    path('', views.index, name='index'), 
    path('signup/', views.signup_view, name='signup'),  
    path('accounts/login/', LoginView.as_view(), name='login'),  
    path('accounts/profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),  
    path('logout/', views.logout_view, name='logout'),  
    
    # Booking URLs
    path('bookings/', views.bookings, name='bookings'),
    path('bookings/add/', views.add_booking, name='add_booking'),
    path('edit_booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('delete_booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),

    # Passenger URLs
    path('passengers/', views.passengers, name='passengers'),
    path('passengers/add/', views.add_passenger, name='add_passenger'),
    path('edit_passenger/<int:passenger_id>/', views.edit_passenger, name='edit_passenger'),
    path('delete_passenger/<int:passenger_id>/', views.delete_passenger, name='delete_passenger'),

    # Employee URLs
    path('employees/', views.employees, name='employees'),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('edit_employee/<int:employee_id>/', views.edit_employee, name='edit_employee'),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),

    # Airport URLs
    path('airports/', views.airports, name='airports'),
    path('airports/add/', views.add_airport, name='add_airport'),
    path('edit_airport/<int:airport_id>/', views.edit_airport, name='edit_airport'),
    path('delete_airport/<int:airport_id>/', views.delete_airport, name='delete_airport'),

    # Aircraft URLs
    path('aircrafts/', views.aircrafts, name='aircrafts'),
    path('aircrafts/add/', views.add_aircraft, name='add_aircraft'),
    path('edit_aircraft/<int:aircraft_id>/', views.edit_aircraft, name='edit_aircraft'),
    path('delete_aircraft/<int:aircraft_id>/', views.delete_aircraft, name='delete_aircraft'),

    # Flight URLs
    path('flights/', views.flights, name='flights'),
    path('flights/add/', views.add_flight, name='add_flight'),
    path('edit_flight/<int:flight_id>/', views.edit_flight, name='edit_flight'),
    path('delete_flight/<int:flight_id>/', views.delete_flight, name='delete_flight'),

    # Schedule URLs
    path('schedules/', views.schedules_list, name='schedules'),
    path('schedules/add/', views.add_schedule, name='add_schedule'),
    path('edit_schedule/<int:schedule_id>/', views.edit_schedule, name='edit_schedule'),
    path('delete_schedule/<int:schedule_id>/', views.delete_schedule, name='delete_schedule'),

    # Ticket URLs
    path('tickets/', views.tickets_list, name='tickets'),
    path('tickets/add/', views.add_ticket, name='add_ticket'),
    path('edit_ticket/<int:ticket_id>/', views.edit_ticket, name='edit_ticket'),
    path('delete_ticket/<int:ticket_id>/', views.delete_ticket, name='delete_ticket'),

    # Route URLs
    path('routes/', views.routes_list, name='routes'),
    path('routes/add/', views.add_route, name='add_route'),
    path('edit_route/<int:route_id>/', views.edit_route, name='edit_route'),
    path('delete_route/<int:route_id>/', views.delete_route, name='delete_route'),

    # Payment URLs
    path('payments/', views.payments_list, name='payments'),
    path('payments/add/', views.add_payment, name='add_payment'),
    path('edit_payment/<int:payment_id>/', views.edit_payment, name='edit_payment'),
    path('delete_payment/<int:payment_id>/', views.delete_payment, name='delete_payment'),

    # Flight Crew URLs
    path('flightcrew/', views.flightcrew_list, name='flightcrew'),
    path('flightcrew/add/', views.add_flightcrew, name='add_flightcrew'),
    path('edit_flightcrew/<int:crew_id>/', views.edit_flightcrew, name='edit_flightcrew'),
    path('delete_flightcrew/<int:crew_id>/', views.delete_flightcrew, name='delete_flightcrew'),

    # Dashboard URL
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard
]

