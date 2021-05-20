from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flights,Passenger
# Create your views here.
def index(request):
    return render(request, 'flights/index.html',{
    "flights":Flights.objects.all() #saving all flights in "flights variable to loop over in the template"
    }
    )
#dont't forget to add the .html
def flight(request, flight_id):
    flight = Flights.objects.get(pk=flight_id)
    passenger = flight.passengers.all()    #quering all the passengers on aspecific flight using the relataed name "passengers"
    return render(request, "flights/flight.html",{
    "flight": flight,
    "passenger":passenger,
    "non_passengers": Passenger.objects.exclude(flights=flight).all()#getting every one not on the flight .all()
    })

def book(request, flight_id):
    #we should have added error checking
    if request.method == "POST":
        flight  = Flights.objects.get(pk=flight_id) #objects is a plural sir
        p_id = request.POST["passenger"]
        print("----",p_id,"----")
        passenger = Passenger.objects.get(pk=int(p_id))#quering passenger with the entered id in the book.html template
        passenger.flights.add(flight)#adding passenger to a flight
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))#reverse engeineer the url using the args, think of it like taking an argument from command line


    #create passenger
    #add passenger to the flight
    #link back to the index or flight page
