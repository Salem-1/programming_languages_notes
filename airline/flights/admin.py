from django.contrib import admin
from .models import Flights, Airport, Passenger # remember to import the lovely classes before using them down here sir

class FlightAmdin(admin.ModelAdmin): #you can figure all of those tricks by reading django documentation
    list_display=("origin","destination", "duration")
    #changin the way flights displayed on admin panel

#changing the passenger table display in the admin panel
#managing the many to many relationship
class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal =("flights",)

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flights, FlightAmdin)
admin.site.register(Passenger, PassengerAdmin)
