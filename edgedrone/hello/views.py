from django.http import HttpResponse
#this function return HttpResponse to the client
from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request,"hello/index.html")

def ahmed(request):
    return HttpResponse("Hello, ya abo 7mied")

def salem(request):
    return HttpResponse("Hello, ya abo salem")

def greet(request, name):
    return render(request,"hello/greet.html",{
    "name":name.capitalize()  # providing additional context 
    })
