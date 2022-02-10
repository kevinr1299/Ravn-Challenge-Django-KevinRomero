from starwars.utils.serializers import GenerateModelSerializer

from starwars.vehicles.models import Vehicle


VehicleSerializer = GenerateModelSerializer(Vehicle, 'vehicles:vehicle')
