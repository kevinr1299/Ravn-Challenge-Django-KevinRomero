from django.urls import path

from starwars.vehicles.views import VehicleRetrieveView

urlpatterns = [
    path('<int:pk>/', VehicleRetrieveView.as_view(), name='vehicle'),
]
