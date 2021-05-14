from django.shortcuts import render, HttpResponse
import datetime
# Create your views here.

def index(request):
    now = datetime.datetime.now()
    if now.month == 1 and now.day == 1:
        result = "yes"

    else:
        result = "NO"
    return render(request, "newyear/index.html",
    {
    "result": result
    })
