from django.shortcuts import render
from .models import ParkingSpot
from .forms import ParkingSpotForm


# Create your views here.

def index(request):
    return render(request, 'parkmap/base.html')

def parking_spot_create_view(request):
    form = ParkingSpotForm(request.POST or None)
    if form.is_valid():
        form.save()
    
    context = {'form': form}

    return render(request, 'parkmap/form.html', context)

def about(request):
    return render(request, 'parkmap/about.html')

def findParking(request):
    return render(request, 'parkmap/findParking.html')

