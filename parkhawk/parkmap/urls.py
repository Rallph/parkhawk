from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.parking_spot_create_view),
    
    path('about', views.about, name='about'),
    path('find-parking', views.findParking, name='findParking')
]