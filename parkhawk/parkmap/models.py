from django.db import models

# Create your models here.
class ParkingSpot(models.Model):
    location = models.CharField(max_length=140) # street, possibly address
    price = models.DecimalField(max_digits=5,decimal_places=2) # price of space
    hours_start_time = models.TimeField() # no way to represent time range that I could find
    hours_end_time = models.TimeField()   # so making start hour and end hour separate
    note = models.CharField(max_length=500) # note for listing creator to leave for others

    def __str__(self):
        return "{0}\t{1}\t{2}\t{3}\t{4}".format(self.location, self.price, self.hours_start_time, self.hours_end_time, self.note)