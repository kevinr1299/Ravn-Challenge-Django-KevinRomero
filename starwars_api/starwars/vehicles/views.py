from rest_framework.generics import RetrieveAPIView

from starwars.vehicles.models import Vehicle
from starwars.vehicles.serializer import VehicleSerializer


class VehicleRetrieveView(RetrieveAPIView):

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
