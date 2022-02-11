from django.db import models

from starwars.utils.models import PrintShowsName


class HairColor(PrintShowsName, models.Model):

    name = models.CharField(max_length=50, unique=True)


class SkinColor(PrintShowsName, models.Model):

    name = models.CharField(max_length=50, unique=True)


class EyeColor(PrintShowsName, models.Model):

    name = models.CharField(max_length=50, unique=True)


class Gender(PrintShowsName, models.Model):

    name = models.CharField(max_length=50, unique=True)


class Specie(PrintShowsName, models.Model):

    name = models.CharField(max_length=50, unique=True)


class World(PrintShowsName, models.Model):

    name = models.CharField(max_length=50, unique=True)
