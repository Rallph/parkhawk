from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
    path('form/', views.parking_spot_create_view)
    
=======
    path('about', views.about, name='about'),
    path('find-parking', views.findParking, name='findParking')
>>>>>>> e95ea0ac73b098ffde2efe1bc524fe05cf94af73
]