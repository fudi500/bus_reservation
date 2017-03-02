from django.db import models
from django.utils import timezone

class Bus(models.Model): # Base model of Bus

    description = models.CharField(max_length=200)
    brand = models.CharField(max_length=150)
    plate_nr = models.CharField(max_length=10)
    people_capacity = models.IntegerField()
    price_per_km = models.DecimalField(max_digits=5, decimal_places=2)
    available_for_cutomers = models.BooleanField(default=True)

    def __str__(self):
        return self.plate_nr


class Client(models.Model):
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=15)
    clientEmail = models.CharField(max_length=15)
    clientPhone = models.CharField(max_length=15)

    def __str__(self):
        return self.lastName



class Reservation(models.Model):
    reBusID = models.ForeignKey( 'Bus',blank=True, null=True)
    reClientID = models.ForeignKey( 'Client',blank=True, null=True)
    reDate = models.DateTimeField(blank=True, null=True) #not used yet
    km = models.IntegerField()
    details = models.CharField(max_length=200)

    def __str__(self):
        return self.details
