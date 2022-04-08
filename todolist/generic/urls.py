from django.contrib import admin
from django.urls import path,include
from .views import AddProject
from generic import views

urlpatterns = [
    path('add/',AddProject.as_view()),
    
]
