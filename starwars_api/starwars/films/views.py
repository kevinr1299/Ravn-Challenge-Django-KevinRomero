from rest_framework.generics import RetrieveAPIView

from starwars.films.models import Film
from starwars.films.serializer import FilmSerializer


class FilmRetrieveView(RetrieveAPIView):

    queryset = Film.objects.all()
    serializer_class = FilmSerializer
