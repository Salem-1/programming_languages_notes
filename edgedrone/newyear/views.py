from django.shortcuts import render, HttpResponse
import datetime
# Create your views here.

def index(request):
    now = datetime.datetime.now()
    month = now.month
    day = now.day
    result = day + month
    return render(request, "newyear/index.html",
    {
    "result": result
    })
