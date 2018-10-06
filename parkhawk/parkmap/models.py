from django.db import models

# Create your models here.
class ParkingSpot(models.Model):
    location = models.CharField(max_length=140) # street, possibly address
    price = models.DecimalField() # price of space
    hours_start_time = models.TimeField() # no way to represent time range that I could find
    hours_end_time = models.TimeField()   # so making start hour and end hour separate
    note = models.CharField(max_length=500) # note for listing creator to leave for others