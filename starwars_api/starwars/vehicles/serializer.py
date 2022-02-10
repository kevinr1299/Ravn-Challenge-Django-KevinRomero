from starwars.utils.serializers import get_serializer_from_model

from starwars.vehicles.models import Vehicle


VehicleSerializer = get_serializer_from_model(Vehicle, 'vehicles:vehicle')
