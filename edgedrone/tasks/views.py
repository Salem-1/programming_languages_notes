from django.shortcuts import render

tasks = ["foo", "bar", "baz"]
# Create your views here.

def index(request):
    return render(request, "tasks/index.html",
    {
        "tasks": tasks
    })

def add(request):
    #new = item.get.something("newtask")
    #tasks.append(new)
    return render(request, "tasks/add.html")
