from django.forms import ModelForm
from .models import ParkingSpot

class ParkingSpotForm(ModelForm):
    class Meta:
        model = ParkingSpot
        fields = ['location', 'price', 'hours_start_time', 'hours_end_time', 'note']
        

