from starwars.utils.serializers import GenerateModelSerializer

from starwars.films.models import Film

FilmSerializer = GenerateModelSerializer(Film, 'films:film')
