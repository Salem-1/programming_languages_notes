# if you made a good test script it will save you the hasle of testing manully,
#aslo it will help you if you made modification in the application not to get lost
from django.test import Client, TestCase
#running theose tset through manage.py,      in the command line , run> python manage.py test
from .models import Airport , Flights, Passenger
from django.db.models import Max
# Create your tests here.
class FlightTestCase(TestCase):

    def setUp(self):
        """building dummy data to test our application a way from our initial database"""

        #create airport
        a1 = Airport.objects.create(code="AAA", city="city A")
        a2 = Airport.objects.create(code="BBB", city="city B")

        #create Flights
        Flights.objects.create(origin=a1, destination=a2, duration=100)
        Flights.objects.create(origin=a1, destination=a1, duration=200)
        Flights.objects.create(origin=a1, destination=a2, duration=-100)

    #running tests on arrivasl, departures, validity of the Flights

    def test_departure_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.departures.count(), 3)

    def test_arrivals_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.arrivals.count(), 1)

    def test_valid_flight(self):
        a1 = Airport.objects.get(code="AAA")
        a2 = Airport.objects.get(code="BBB")
        f = Flights.objects.get(origin=a1, destination=a2,duration = 100)
        self.assertTrue(f.is_valid_filght())

        def test_invalid_flight_destination(self):
            a1 = Airport.objects.get(code="AAA")
            a2 = Airport.objects.get(code="BBB")
            f = Flights.objects.get(origin=a1, destination=a1)
            self.assertFalse(f.is_valid_filght())

        def test_valid_flight_duration(self):
            a1 = Airport.objects.get(code="AAA")
            a2 = Airport.objects.get(code="BBB")
            f = Flights.objects.get(origin=a1, destination=a2,duartion = -100)
            self.assertFalse(f.is_valid_filght())

        #tetsting the webpages
        def test_index(self):
            c = Client() # representing the client who is using the aooliction
            response = c.get("/flights/") # making request to the flights page as we added three filhgts already upthere
            self.assertEqual(response.status_code, 200) # making sure that the responses was successful
            self.assertEqual(response.contetxt("flights").count(), 3)

        #testing the flight page
        def test_valid_flight_page(self):
            a1 = Airport.objects.get(code="AAA")
            f = Flights.objects.get(origin=a1, destination=a1)
            #making request to test  the page now
            c = Client() # creating a virtual Client
            response  = c.get(f"/flights/{f.id}") # requesting fligth page by it;s flihgt id
            self.assertEqual(response.status_code, 200)


    #test invalid filght page
    def test_invalid_flight_page(self):
        max_id = Flights.objects.all().aggregate(Max("id"))["id__max"]
        c = Client()
        response = c.get(f"/flights/{max_id + 1}")#trying to acces an id which is not there
        self.assertEqual(response.status_code, 404) # invalid page code #remember the self. sir

    #testing the passengers page
    def test_flight_page_passengers(self):
        f = Flights.objects.get(pk=1)  # don't forget the get sir
        p =  Passenger.objects.create(first="Ahmed", last="Salem")
        f.passengers.add(p)

        c = Client()
        response = c.get(f"/flights/{f.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["passenger"].count(), 1)


    def test_flight_page_non_passengers(self):
        f = Flights.objects.get(pk=1)
        p =  Passenger.objects.create(first="Ahmed", last="Salem")

        c = Client()
        response = c.get(f"/flights/{f.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["non_passengers"].count(), 1)
