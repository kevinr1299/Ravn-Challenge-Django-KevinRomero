from rest_framework.generics import RetrieveAPIView

from starwars.people.models.catalogues import (
    EyeColor,
    Gender,
    HairColor,
    SkinColor,
    Specie,
    World,
)
from starwars.people.serializers.catalogues import (
    EyeColorSerializer,
    GenderSerializer,
    HairColorSerializer,
    SkinColorSerializer,
    SpecieSerializer,
    WorldSerializer,
)


class EyeColorRetrieveView(RetrieveAPIView):

    queryset = EyeColor.objects.all()
    serializer_class = EyeColorSerializer


class GenderRetrieveView(RetrieveAPIView):

    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class HairColorRetrieveView(RetrieveAPIView):

    queryset = HairColor.objects.all()
    serializer_class = HairColorSerializer


class SkinColorRetrieveView(RetrieveAPIView):

    queryset = SkinColor.objects.all()
    serializer_class = SkinColorSerializer


class SpecieRetrieveView(RetrieveAPIView):

    queryset = Specie.objects.all()
    serializer_class = SpecieSerializer


class WorldRetrieveView(RetrieveAPIView):

    queryset = World.objects.all()
    serializer_class = WorldSerializer
