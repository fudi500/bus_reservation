from django.db import models
from django.utils import timezone

class Bus(models.Model):
    author = models.ForeignKey('auth.User')
    description = models.CharField(max_length=200)
    brand = models.CharField(max_length=150)
    plate_nr = models.CharField(max_length=10)
    people_capacity = models.IntegerField()
    price_per_km = models.IntegerField()
    available_for_cutomers = models.BooleanField(default=True)

    def __str__(self):
        return self.plate_nr
