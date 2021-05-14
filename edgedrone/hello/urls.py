from django.urls import path

from . import views
#import the views file from the current directory
 #create a list urlpatterns that contain all urls for this application
urlpatterns = [
    path ("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path ("ahmed", views.ahmed, name="ahmed"),
    path ("salem", views.salem, name="salem")
]
