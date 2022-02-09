from django.db import models

from starwars.people.models.person import Person


class Film(models.Model):

    name = models.CharField(max_length=50)
    characters = models.ManyToManyField(Person)
