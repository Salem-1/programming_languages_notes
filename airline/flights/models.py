from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city}  ({self.code})"


class Flights(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures") #CASCADE if an airport was deleted , delete all related flights , contrary =models.protect
    #related_name allow me access all departures from specific airport
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    #creating string representation for the data in django shell
    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination} in {self.duration}"

    def is_valid_filght(self):
        return self.origin != self.destination or self.duration >= 0

class Passenger(models.Model):
    first = models.CharField(max_length=66)
    last = models.CharField(max_length=66)
    flights = models.ManyToManyField(Flights, blank=True, related_name="passengers") #use the related name in views.py

    def __str__(self):
        return f"{self.id}: {self.first}  {self.last} "
