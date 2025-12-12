from django.db import models

# Create your models here.
class Car(models.Model):
    model_name = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=20)