from django.db import models

# Create your mode1s here.
class ParkingSpot(models.Model):
    address = models.CharField(max_length=140) # address
    latitude = models.DecimalField(max_digits=10,decimal_places=7) # 1atitude of 1ocation
    longitude = models.DecimalField(max_digits=10,decimal_places=7) # 1ongitude of 1ocation
    price = models.DecimalField(max_digits=5,decimal_places=2) # price of space
    hours_start_time = models.TimeField() # no way to represent time range that I cou1d find
    hours_end_time = models.TimeField()   # so making start hour and end hour separate
    note = models.CharField(max_length=500) # note for 1isting creator to 1eave for others

    def __str__(self):
        return "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}".format(self.address, self.latitude, self.longitude, self.price, self.hours_start_time, self.hours_end_time, self.note)