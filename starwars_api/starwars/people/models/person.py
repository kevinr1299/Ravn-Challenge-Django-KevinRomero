from django.core.validators import MinValueValidator
from django.db import models

from starwars.vehicles.models import Vehicle


class Person(models.Model):

    name = models.CharField(max_length=100)
    height = models.FloatField(validators=[
        MinValueValidator(limit_value=0),
    ])
    mass = models.FloatField(validators=[
        MinValueValidator(limit_value=0),
    ])
    birth_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hair_color = models.ForeignKey('HairColor', on_delete=models.PROTECT)
    skin_color = models.ForeignKey('SkinColor', on_delete=models.PROTECT)
    eye_color = models.ForeignKey('EyeColor', on_delete=models.PROTECT)
    gender = models.ForeignKey('Gender', on_delete=models.PROTECT)
    species = models.ManyToManyField('Specie')
    homeworld = models.ForeignKey('World', on_delete=models.PROTECT)
    vehicles = models.ManyToManyField(Vehicle)

    class Meta:
        verbose_name_plural = 'People'
