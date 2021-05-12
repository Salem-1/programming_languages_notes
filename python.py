print("Hello, world")
#print string to the terminal
x = 1 # integer
y = "hi"  #string
c = 2.3  # floeat
d = True  # boolean
e = None #lack of value
#assigning variables without type specisification


#taking input
name = input("Name: ")
print("hello " +name)
print(f"Hello {name}")


#conditions
n = int(input("number"))    #converting the string input to integer
if n > 0:
    print("n is positive")
elif n < 0 :
    print("n is negative")
else:
    print("n = 0")



#data equences

name = "Ahmed"
print(name[0])
#expected output os "A"
print(name[1])
#expected output os "h"


#lists
names =['ahemd', 'mohaemd','saelm']
print(names)
#output ['ahemd', 'mohaemd','saelm']
#lists are mutables
print(namesp[0])
#output 'ahemd'
list.append("Amer")
#add value to an existing list as last new index
names.sort()
#will sort your list automatically



#tuples are immutanle
coordinate = (10.0,20.0)

#set ->collection of unique vales, no order however all values are unique like usernames
s = set()
#creating an empty set
set.add(1)
set.add(2)
set.add(3)
set.add(4)
#adding elements to teh settings

s.remove(2)
#removing item from the set

#how many elements in the sett
print(len(s))


#dict ->collection of key value pair, like the actual physical dictionnary
d = {"key": "value"}
d['2nd key'] = 'value 2'

print(d["key"])
#expected output "value"




#looping

#for loop
for i in range(0,6):
    print(i)

for name in names:
    print(name)

for letter in "Ahmed":
    print(letter)

################################################functions####################################################
#squaring a numner
def square(n):
    return n * n

for i in range(10):
    print(f"the square of {i} is {square(i)}")

#expected output , the square of i, i will not calculate it for you :)

#importing from other modules(files)
#option 1
#from squares import square as s
print(square(2))

#OPTION 2
#import squares
#print(squares.square(2))

 #import csv, math,    ....ect


 ############################################classes#########################################################
 #creating your new object, think of it as a template of  atype of objects

 class Point():
     """creating x,y cordinate pointy"""
     def __init__(self ,input1 ,input2):
         #it will be called every time the class called
         #when i create a pioint what should happen?
         self.x = input1 #store the argument of input1 as x
         self.y = input2

p = Point(2,8) #assining variable to our class
print(p.x)# accessing the data
print(p.y)

#one more example
class Flight():
    """monitoring flight capacity"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def adding_passenger(self, name):
        if not self.open_seats:
            return False

        self.passengers.append(self.name)
        return True
    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(3)

for person in names:
    #sucess = flight.adding_passenger(person)
    if flight.adding_passenger(person):
        print(f"{person} added to the flight successfully")
    else:
        print(f"No more available seats for {person}")


#####################decorator################# functional programming###########think of it like sandwich

def announce(f):
    def wrapper():
        print("about to run the function ....")
        f()
        print("Done running function")

#wrapping the function
@announce
def hello():
    print("Hello world")
hello()
#expected out put
#"about to run the function ...."
#"Hello world"
#"Done running function"

###################lamda#############one time function

people = [
    {"name": "Ahmed", "num": 1},
    {"name": "mohamed", "num": 2},
    {"name": "salem", "num": 3}
]

#how to sort?!
#people.sort() will give type error
# one way to solve this problem

def f(person):
    return person["name"]

people.sort(key=f)
print(people)
#should print the people list sorted by name

#another approach to do this is using lambda
people.sort(key=lambda person:person["name"])
print(people)
#expected same output as above


##########################handling exceptions###############
import sys
#for example
x = int(input("X: "))
y = int(input("Y: "))
#handling the string output or zero division error

try:
    x = int(input("X: "))
    y = int(input("Y: "))
except ZeroDivisionError or ValueError:
    print("Error:cannot define by zero or value error")

    sys.exit(1)
