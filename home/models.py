from django.db import models

# Create your models here.
class vehicle(models.Model):
    model_name = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.model_name} - {self.license_plate}"
