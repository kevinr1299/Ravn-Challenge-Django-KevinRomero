from django.db import models

from starwars.people.models.person import Person
from starwars.utils.models import PrintShowsName


class Film(PrintShowsName, models.Model):

    name = models.CharField(max_length=50, unique=True)
    characters = models.ManyToManyField(Person, blank=True)
