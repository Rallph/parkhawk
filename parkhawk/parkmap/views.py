from django.shortcuts import render
from django.views.generic.list import ListView
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

class ParkingListView(ListView):

    model = ParkingSpot

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
