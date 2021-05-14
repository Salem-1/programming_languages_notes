from django import forms
from django.http import HttpResponseRedirect #redirect to specific url
from django.urls import reverse # reverse engineer urls as following reverse("appname: template")
from django.shortcuts import render


#class for genrating forms, i believe in larger projects it should be in a separate module(file)
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task") #character field input & the label is what going to appear on top of the empty field
    priority = forms.IntegerField (label="Priority", min_value=1, max_value=10)

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html",
    {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST": # check if the user submitted the form
        form = NewTaskForm(request.POST)  #saving the submitted form in form variable

        # checking if the submitted data is valid(built  in function in django)
        if form.is_valid():
            task = form.cleaned_data["task"] # saving the inputted task in task variable
            priority = form.cleaned_data["priority"]
            request.session["tasks"] += [task] # adding the inputted task to our session as separate list
            return HttpResponseRedirect(reverse("tasks:index")) # the reverse() reverse engineer the url
            #redirect to index of tasks application
        else:
            return render(request, "tasks/add.html", {
            "form": form
            })

    return render(request, "tasks/add.html",
    {
    "form":NewTaskForm()
    })
