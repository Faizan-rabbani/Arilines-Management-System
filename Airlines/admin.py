from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Employee)
admin.site.register(models.FlightCrew)
admin.site.register(models.Airport)
admin.site.register(models.Aircraft)
admin.site.register(models.Flight)
admin.site.register(models.Passenger)
admin.site.register(models.Booking)
admin.site.register(models.Payment)
admin.site.register(models.Ticket)
admin.site.register(models.Route)
admin.site.register(models.Schedule)