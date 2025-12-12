from django.shortcuts import render
from . import models
# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def list_of_cars(request):
    cars = models.Car.objects.all()
    return render(request, 'home/list_of_cars.html', {'cars': cars})