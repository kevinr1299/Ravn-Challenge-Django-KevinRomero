from starwars.utils.serializers import get_serializer_from_model

from starwars.films.models import Film

FilmSerializer = get_serializer_from_model(Film, 'films:film')
