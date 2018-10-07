from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'parkmap/base.html')

def about(request):
    return render(request, 'parkmap/about.html')

def findParking(request):
    return render(request, 'parkmap/findParking.html')