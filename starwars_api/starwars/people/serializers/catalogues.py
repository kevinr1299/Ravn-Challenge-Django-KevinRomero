from starwars.people.models.catalogues import (
    EyeColor,
    Gender,
    HairColor,
    SkinColor,
    Specie,
    World,
)
from starwars.utils.serializers import get_serializer_from_model


EyeColorSerializer = get_serializer_from_model(
    EyeColor,
    'catalogues:eye_color',
)
GenderSerializer = get_serializer_from_model(Gender, 'catalogues:gender')
HairColorSerializer = get_serializer_from_model(
    HairColor,
    'catalogues:hair_color',
)
SkinColorSerializer = get_serializer_from_model(
    SkinColor,
    'catalogues:skin_color',
)
SpecieSerializer = get_serializer_from_model(Specie, 'catalogues:specie')
WorldSerializer = get_serializer_from_model(World, 'catalogues:world')
