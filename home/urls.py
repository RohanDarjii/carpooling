from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='home'),
    path('cars/', views.list_of_cars, name='list_of_cars'),
]
