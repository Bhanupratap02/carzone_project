
from django.urls import path
from . import views
urlpatterns = [
    path('', views.cars, name='cars'),
    path('<int:pk>/', views.car_details, name='car_details'),
   
]