from django.db import models


class HairColor(models.Model):

    name = models.CharField(max_length=50)


class SkinColor(models.Model):

    name = models.CharField(max_length=50)


class EyeColor(models.Model):

    name = models.CharField(max_length=50)


class Gender(models.Model):

    name = models.CharField(max_length=50)


class Specie(models.Model):

    name = models.CharField(max_length=50)


class World(models.Model):

    name = models.CharField(max_length=50)
