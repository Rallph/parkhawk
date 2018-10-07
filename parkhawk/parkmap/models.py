from django.db import models

# Create your models here.
class ParkingSpot(models.Model):
    address = models.CharField(max_length=140) # address
    latitude = models.DecimalField(max_digits=3,decimal_places=7) # latitude of location
    longitude = models.DecimalField(max_digits=3,decimal_places=7) # longitude of location
    price = models.DecimalField(max_digits=5,decimal_places=2) # price of space
    hours_start_time = models.TimeField() # no way to represent time range that I could find
    hours_end_time = models.TimeField()   # so making start hour and end hour separate
    note = models.CharField(max_length=500) # note for listing creator to leave for others