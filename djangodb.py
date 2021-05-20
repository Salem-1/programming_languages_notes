#notes about database in django framework
#models : python clas representing data I want to use in database
 #open models.py file
 #for example
 from django.db import models

# Create your models here.
class fligts(models.Model):
    origin = models.CharField(max_length=64) #creating column char type
    destination = models.CharField(max_length=64)
    duration = models.IntegerField() #creating column int type

    #creating string representation for the data in django shell
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

    ################then make migrations to tell django to apply our changes into the database
#in the command line
python manage.py makemigrations
#mogration will be reflectedin migrations directory inside the application
#then applying migrations, also in the terminal
python manage.py migrate

###################to play with the database you don't have to opent the db.sqlite3 files
###instead you can use the django shell , in the terminal type
python manage.py shell
#in the shell you can write python commands that will be executed on the webapplication
#step1 import the class you created in the models.py file
from appname.models import Class_name

#inserting into tables
variable = Class_name(var1 = value, var2 =value2)
#saving the insertions
variable.save()

flight =Flights.objects.all() ##assigning variable to all data saved as objects in this class
flights
#expected out put is string representation of that database
flight = flight.first()
#allow me to inquiry data from flight table

#then you can start ask flight quries LIKE
#what is your id
flight.id
#what is your origin
flight.origin
#what is your destination
flight.destination

#delete the flight
flight.delete
#excedra

################
##new model.py
from django.db import models

# saving airport as separate class.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city}  ({self.code})"

Each flight will have origin and destination of an airport class
class Flights(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures") #CASCADE if an airport was deleted , delete all related flights , contrary =models.protect
    #related_name allow me access all departures from specific airport
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    #creating string representation for the data in django shell
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

## after applying the makemigrations and migrate
# in the django shell
from flights.models import *
jfk = Airport(code="JFK", city="New York") #adding new airport
jfk.save()
lhr = Airport(code="LHR", city = "London")
lhr.save()
cdg = Airport(code="CDG", city = "Paris")
cdg.save()
nrt = Airport(code="NRT", city = "Tokyo")
nrt.save()
f = Flights(origin = jfk, destination= lhr, duration = 1) #adding flights
#accessing flights info.
>> f.save()
>> f.origin.code
JFK'
>> f.origin.city
New York'
<Flights: 1: New York  (JFK) to London  (LHR)>
>>> f.origin
<Airport: New York  (JFK)>

#searching for property iside class
Airport.objects.filter(city="New York")#inside the bractes but the search condition
Airport.objects.get(city="New York") == Airport.objects.filter(city="New York").first()#gives the first result like LIMIT 1 in SQL

#Django was intially developed for news organizations, that's why it's easy to manipulate database with it
########################setup super user , in the terminal
python manage.py createsuperuser
######## to use model in the admin panles, open app/admin.py
from .views import *
admin.site.register(Class_name)
##########running admin site , run the server then , access url/admin
