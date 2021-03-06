from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class Bus(models.Model): # Base model of Bus
    description = models.CharField(max_length=200)
    brand = models.CharField(max_length=150)
    plate_nr = models.CharField(max_length=10)
    people_capacity = models.IntegerField()
    price_per_km = models.DecimalField(max_digits=5, decimal_places=2)
    available_for_cutomers = models.BooleanField(default=True)
    currentDriver = models.ForeignKey('Driver',blank=True, null=True)

    def __str__(self):
        return self.plate_nr


class Driver(models.Model):
    driverName = models.CharField(max_length=30)
    driverPhone = models.CharField(max_length=30)

    def __str__(self):
        return self.driverName

class Reservation(models.Model):
    reBusID = models.ForeignKey( 'Bus')
    clientName = models.CharField(max_length=30)
    clientEmail = models.EmailField()
    clientPhone = models.CharField(max_length=15)

    reDate = models.DateField(help_text='Date of reservation')
    EndDate = models.DateField(blank=True, null=True)
    numOfDays = models.IntegerField(blank=True, null=True)
    km = models.IntegerField(validators=[
            MinValueValidator(0)
        ])
    details = models.CharField(max_length=200)

    def __str__(self):
        return self.details
