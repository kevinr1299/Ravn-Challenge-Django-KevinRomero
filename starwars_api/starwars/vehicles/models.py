from django.db import models

from starwars.utils.models import PrintShowsName


class Vehicle(PrintShowsName, models.Model):

    name = models.CharField(max_length=50)
