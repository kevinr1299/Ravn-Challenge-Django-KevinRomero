from django.db import models

from starwars.utils.models import PrintShowsName


class HairColor(PrintShowsName, models.Model):

    name = models.CharField(max_length=50)


class SkinColor(PrintShowsName, models.Model):

    name = models.CharField(max_length=50)


class EyeColor(PrintShowsName, models.Model):

    name = models.CharField(max_length=50)


class Gender(PrintShowsName, models.Model):

    name = models.CharField(max_length=50)


class Specie(PrintShowsName, models.Model):

    name = models.CharField(max_length=50)


class World(PrintShowsName, models.Model):

    name = models.CharField(max_length=50)
