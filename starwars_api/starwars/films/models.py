from django.db import models


class Film(models.Model):

    name = models.CharField(max_length=50)
    characters = models.ManyToManyField('People')
