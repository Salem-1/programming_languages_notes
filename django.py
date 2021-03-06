#Bism ellah elrahman elraheem
#Django framework notes !!!
#most code in this document are instruction not code to run
creating virtual environment:
1-open powershell
2-go to the needed path
3-python -m venv <filename>

#activating virtual environment
in the terminal
1-Set-ExecutionPolicy RemoteSigned -scope process
2-<path>/scripts/activate
#deactivating the virtual environment
in the terminal type:
deactivate
#############################################--{{Django}}--###########################################################
                                                --------
#Django allow us to write python code to dynamically generate HTML and css
#installing django- in the virtual environment type
pip3 install django

#creating django project
django-admin startproject <project-name>


#we will not need to touch manage.py file but will use it to execute orders
#settings.py has important configuration settings we might modify as we are adding features to our application
#urls.py like a table of content for our application
#django project consits of multiple applications,think of it as making each service on your website as a separate app

#running the webapplication, in the terminal type
python manage.py runserver


#django project consits of multiple applications,think of it as making each service on your website as a separate app
#creating app in Django
python manage.py startapp <appname>

#the views.py file controls what users see or what gets rendered to the user

#installing the created app in django project
1-open settings.py file
2-ctr+f "INSTALLED_apps" #this is list with all installed apps usally on line 33
3- add the app name as item in the INSTALLED_APP list like this
INSTALLED_APP = [
   'created_app_name',
   .
   .
   .
]
4-don't forget to save the file.


#how to let my app do something?
#by coding in views.py , think of each view as something user want to see
###################################################views.py##########################
#to create a view in django we define a function
from django.http import HttpResponse
#this function return HttpResponse to the client

def index(request): #this function take the http_request that the user made to access our web server as an argument
#then we need to look inside that request to get more information
    return render(request, "hello/index.html") # then create this path inside the hello directory"templates/hello/index.html"
                          #the use of hello/ is to diffrentiate which index for which applicaiton
def greet(request, variable): #it can take variables 3ady
    return HttpResponse(f"Hello, {variable}")

def greethim(request, variable): #it can take variables 3ady
    return render(request, "hello/greethim.html",{
    "name":name   # providing all variables you want to give your template access to
    })
#but what url should the user visit to get that response and run the index function?
#to do this we will need to create a urls.py file to handle the urls for each function
##############################urls.py##############
#to create urls first you need to  in the application url file
from django.urls import path

from . import views #import the views file from the current directory
 #create a list urlpatterns that contain all urls for this application
urlpatterns = [
    path ("", #this is the default function, think of it as the first page in the app
    views.index #showing what function in the views.py should be accessed(called)
    ,name="index")#this is an optional name for the path,
    ,path("anotherpath", views.anotherpath, name = anotherpath )
    ,path("<str:variable>", #placeholder for the variable name
    views.greet, name="greet")
]

###################appname/urls.py
#in the main project url
from django.urls import include, path
#then open urls.py for the main project
#then add

app_name = "applicationname"
urlpatterns = [

    ,path('applicationname/',include("applicationname.urls"))
]

#####################################html templates##############
################static-styles.css###################
#make the following file path inside the app directory
#static/appname/styles.css
#for example grretme
{%load static%}
#laoding the static file
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
     #using the css static file in our template
    <link rel="stylesheet" href="{% static 'appname/styles.css' %}">

    <title>hello</title>
  </head>
  <body>
    <h1>Ahlan ya {{name}}</h1> # providing html with your variables inside {{}}
    #using conditions in html template Django/jinja syntax
    {%if condition%}
    do something
    {%else%}
    do otherthing
    {%endif%}

    ##looping
    {%for item in items %}
    {{item}}
    {% endfor %}
  </body>
</html>
################using layout.html to make life easY####################
{%load static%}
#laoding the static file
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
     #using the css static file in our template
    <link rel="stylesheet" href="{% static 'appname/styles.css' %}">

    <title>hello</title>
  </head>
  <body>
  #here the place where it will be changed in every template
     {% block body %}
     {% endblock %}
     #that's it
  </body>
</html>
#########
#let's implement it on the above
#write the first two lines
{% extends "tasks/layout.html" %}
{% block body %}
#but your page content here
    <h1>Ahlan ya {{name}}</h1> # providing html with your variables inside {{}}
    #using conditions in html template Django/jinja syntax
    {%if condition%}
    do something
    {%else%}
    do otherthing
    {%endif%}

    ##looping
    {%for item in items %}
    {{item}}
    {% endfor %}

    #linking to other page
    <a href="{% url 'appname:index' %}">hyperlinked txt</a>
#after you are done with the page content
#write this line of code
{% endblock %}
######################################taking form inputs######################

#csrf = cross site request frogery
# for example

{% extends "tasks/layout.html" %}
{% block body %}
    <h1>Add task</h1>
    <form action="{% url 'tasks:add' %}" method ="post"> # action is where do I want those inputs to go , method (get or post )
      <input type="text" name="task" >
      <input type="submit" >
      </form>
      <a href="{% url 'tasks:index' %}">view your tasks</a>
  </body>
</html>
{% endblock %}
###################################generating forms in django###################
#remember to always , I mean always make server and client side validation
# in the views filefrom django import forms
from django.http import HttpResponseRedirect #redirect to specific url
from django.urls import reverse # reverse engineer urls as following reverse("appname: template")
from django.shortcuts import render

tasks = ["foo", "bar", "baz"]
# Create your views here.

#class for genrating forms, i believe in larger projects it should be in a separate module(file)
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task") #character field input & the label is what going to appear on top of the empty field
    priority = forms.IntegerField (label="Priority", min_value=1, max_value=10)

def index(request):
    return render(request, "tasks/index.html",
    {
        "tasks": tasks
    })

def add(request):
    if request.method == "POST": # check if the user submitted the form
        form = NewTaskForm(request.POST)  #saving the submitted form in form variable

        # checking if the submitted data is valid(built  in function in django)
        if form.is_valid():
            task = form.cleaned_data["task"] # saving the inputted task in task variable
            priority = form.cleaned_data["priority"]
            tasks.append(task) # adding the inputted task to our list
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
######################
#creating project database tables , in the terminal type
python manage.py migrate

###############################sessions#################
#let's play with sessions in the same views.py file
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
