from starwars.people.models.catalogues import (
    EyeColor,
    Gender,
    HairColor,
    SkinColor,
    Specie,
    World,
)
from starwars.utils.serializers import GenerateModelSerializer


EyeColorSerializer = GenerateModelSerializer(
    EyeColor,
    'catalogues:eye_color',
)
GenderSerializer = GenerateModelSerializer(Gender, 'catalogues:gender')
HairColorSerializer = GenerateModelSerializer(
    HairColor,
    'catalogues:hair_color',
)
SkinColorSerializer = GenerateModelSerializer(
    SkinColor,
    'catalogues:skin_color',
)
SpecieSerializer = GenerateModelSerializer(Specie, 'catalogues:specie')
WorldSerializer = GenerateModelSerializer(World, 'catalogues:world')
